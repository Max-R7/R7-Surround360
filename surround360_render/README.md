# Surround 360 Rendering Software

Surround 360 is a hardware and software system for capturing and rendering 3d (stereo) 360 videos and photos, suitable for viewing in VR. This subdirectory of the project is specific to rendering software.

## Requirements

* The Surround 360 rendering software requires either Linux or Mac OS X

* The essential dependencies of the Surround 360 rendering software are:
  * CMake
  * gflags
  * glog
  * OpenCV 3.0+

* Additional optional functionality depends on:
  * ffmpeg
  * Gooey
  * wx

## Installing Dependencies of the Surround 360 Rendering Software

* After building all of the dependencies and the rendering code itself, there are no further installation steps.

* The build system for the Surround 360 code is CMake.

* This software has been tested on Ubuntu 14.04/16.04 LTS (CMake 3.2.2) and OS X 10.11.5 (using CMake 3.5.1).

* Install CMake (method 2 - Linux only)
```
  sudo apt-get install software-properties-common
  sudo add-apt-repository ppa:george-edison55/cmake-3.x
  sudo apt-get update
  sudo apt-get install cmake && sudo apt-get upgrade cmake
```

* Git is used to download and install packages from source (e.g. OpenCV below). Git may come preinstalled (check using git --version). It is not required if using brew in OS X.

* Install Git (method 1 - Linux only):
```
  sudo apt-get install git
```

* Install Subversion (method 1 - Linux only):
```
  sudo apt install subversion
```

* Install Python (method 1 - Linux only):
```
  sudo apt-get install python
```

* Install gflags (method 1 - Linux only):
```
  sudo apt-get install libgflags2v5 libgflags-dev
```

* Install glog (method 1 - Linux only):
```
  sudo apt-get install libgoogle-glog-dev
`````

* Install folly (method 1):
  see https://github.com/facebook/folly

* Install Ceres (method 1 - Linux only)
  see http://ceres-solver.org/installation.html
```
  sudo apt-get install libatlas-base-dev
  sudo apt-get install libeigen3-dev
  cd ~
  git clone https://ceres-solver.googlesource.com/ceres-solver
  cd ceres-solver
  mkdir ceres-bin
  cd ceres-bin
  cmake ..
  make -j3
  sudo make install
  sudo ln -s /usr/include/eigen3/Eigen /usr/local/include/Eigen
```

* Install OpenCV:
```
  cd ~
  git clone https://github.com/Itseez/opencv.git
  cd opencv
  git checkout tags/3.1.0
  cmake -DWITH_IPP=OFF
  make
  sudo make install
```

* Install ffmpeg (method 1):
  see https://trac.ffmpeg.org/wiki/CompilationGuide
* Install dependencies
  sudo apt-get update
  sudo apt-get -y install autoconf automake build-essential libass-dev libfreetype6-dev libsdl1.2-dev libtheora-dev libtool libva-dev libvdpau-dev libvorbis-dev libxcb1-dev libxcb-shm0-dev libxcb-xfixes0-dev pkg-config texinfo zlib1g-dev

* Install Yasm
  cd ~/ffmpeg_sources
  wget http://www.tortall.net/projects/yasm/releases/yasm-1.3.0.tar.gz
  tar xzvf yasm-1.3.0.tar.gz
  cd yasm-1.3.0
  ./configure 
  --prefix="$HOME/ffmpeg_build" \
  --bindir="$HOME/bin"
  make
  make install
  make distclean

* Install libx264
  cd ~/ffmpeg_sources
  wget http://download.videolan.org/pub/x264/snapshots/last_x264.tar.bz2
  tar xjvf last_x264.tar.bz2
  cd x264-snapshot*
  PATH="$HOME/bin:$PATH" ./configure 
  --prefix="$HOME/ffmpeg_build" \
  --bindir="$HOME/bin" \
  --enable-static \
  --disable-opencl \
  --enable-shared
  PATH="$HOME/bin:$PATH" make
  make install
  make distclean

* Install livbpx
  cd ~/ffmpeg_sources
  wget http://storage.googleapis.com/downloads.webmproject.org/releases/webm/libvpx-1.5.0.tar.bz2
  tar xjvf libvpx-1.5.0.tar.bz2
  cd libvpx-1.5.0
  PATH="$HOME/bin:$PATH" ./configure 
  --prefix="$HOME/ffmpeg_build" \
  --disable-examples \
  --disable-unit-tests \
  --enable-shared \
  PATH="$HOME/bin:$PATH" make
  make install
  make clean


* Install Ffmpeg
  cd ~/ffmpeg_sources
  wget http://ffmpeg.org/releases/ffmpeg-snapshot.tar.bz2
  tar xjvf ffmpeg-snapshot.tar.bz2
  cd ffmpeg
  PATH="$HOME/bin:$PATH" PKG_CONFIG_PATH="$HOME/ffmpeg_build/lib/pkgconfig" ./configure \
  --prefix="$HOME/ffmpeg_build" \
  --pkg-config-flags="--static" \
  --extra-cflags="-I$HOME/ffmpeg_build/include" \
  --extra-ldflags="-L$HOME/ffmpeg_build/lib" \
  --bindir="$HOME/bin" \
  --enable-nonfree \  
  --enable-gpl \
  --enable-libx264 \
  --enable-shared \
  --enable-libvpx 
  PATH="$HOME/bin:$PATH" make
  make install
  make distclean
  hash -r

  cd /etc/ld.so.conf.d/
  sudo vim ffmpeg.conf

#Add one line:
  /home/reality7/ffmpeg_build/lib

  sudo ldconfig

* Install Gooey (method 2 - Linux only):
```
  sudo apt-get install python-pip
  sudo pip install --upgrade pip
  sudo pip install Gooey
  echo "deb http://archive.ubuntu.com/ubuntu wily main universe" | sudo tee /etc/apt/sources.list.d/wily-copies.list
  sudo apt update
  sudo apt install python-wxgtk2.8
  sudo rm /etc/apt/sources.list.d/wily-copies.list
  sudo apt update
``

* (if using accelerated ISP) Install LLVM
```
  cd ~
  svn co https://llvm.org/svn/llvm-project/llvm/branches/release_37 llvm3.7
  svn co https://llvm.org/svn/llvm-project/cfe/branches/release_37 llvm3.7/tools/clang
  cd llvm3.7
  mkdir build
  cd build
  cmake -DLLVM_ENABLE_TERMINFO=OFF -DLLVM_TARGETS_TO_BUILD="X86;ARM;NVPTX;AArch64;Mips;PowerPC" -DLLVM_ENABLE_ASSERTIONS=ON -DCMAKE_BUILD_TYPE=Release ..
  make
  export LLVM_CONFIG=$HOME/llvm3.7/build/bin/llvm-config
  export CLANG=$HOME/llvm3.7/build/bin/clang
```

* (to use accelerated ISP) Install Halide
```
  cd ~
  git clone https://github.com/halide/Halide.git
  cd Halide
  mkdir cmake_build
  cd cmake_build
  export LLVM_ROOT=$HOME/llvm3.7/build
  cmake -DLLVM_BIN=${LLVM_ROOT}/bin -DLLVM_INCLUDE="${LLVM_ROOT}/../include;${LLVM_ROOT}/include" -DLLVM_LIB=${LLVM_ROOT}/lib -DLLVM_VERSION=37 ..
  make
```

## Compiling the Surround 360 Rendering Software

* After installing all of the dependencies as described above, run:
```
  cd <install_path>/surround360/surround360_render
  cmake -DCMAKE_BUILD_TYPE=Release
  make
```

  (to use accelerated ISP):
```
  cd <install_path>/surround360/surround360_render
  cmake -DCMAKE_BUILD_TYPE=Release -DHALIDE_DIR=$HOME/Halide/cmake_build
  make
```

* To test that compilation is successful, run:
```
  ./bin/TestRenderStereoPanorama --help
```

* We recommend configuring CMake to compile in Release mode because the code will execute faster. However, you can also set it up for debug mode with:
```
  cmake -DCMAKE_BUILD_TYPE=Debug
```

* Sometimes it is useful to compile with XCode instead of CMake (e.g., to use its profiling and debugging tools). To do so:
```
  cd <install_path>/surround360/surround360_render
  mkdir XCodeDebug
  cd XCodeDebug
  cmake -DCMAKE_BUILD_TYPE=Debug -G Xcode ..
```

## How the Surround 360 Rendering Software Works

Check out our blog post about how rendering for Surround 360 works here:
https://code.facebook.com/posts/265413023819735


## Join the Surround 360 community

* Website: https://facebook360.fb.com/facebook-surround-360/

See the CONTRIBUTING file for how to help out.

## License

The Surround 360 rendering code is BSD-licensed, as it appears in LICENSE_render.md under /surround360_render. We also provide an additional patent grant.
