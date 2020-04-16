## About

This repository is part of my [student project](https://github.com/cp3-ws1920) for Computational Physics III at the FSU Jena in the winter term 19/20.

It contains some example applications that I used to test/demonstrate the two submodules I wrote during my project, a [delaunay triangulator](https://github.com/cp3-ws1920/triangulator) and a [finite element solver](https://github.com/cp3-ws1920/fem_solver).

## Cloning and compiling

To clone the repository and initialize all submodules:
```
git clone https://github.com/cp3-ws1920/applications --recursive
```

Compilation is easiest using CMake

```
mkdir build
cd build
cmake ..
cmake --build . --target <target>
```

`<target>` can be any of the target names below.

## Applications

### triangulate_poly.cpp

<img src="https://github.com/cp3-ws1920/applications/raw/master/preview.png" width="500" />

Build with `--target triangulate_poly`.

Takes a [.poly](https://www.cs.cmu.edu/~quake/triangle.poly.html) as input and produces a [.node](https://www.cs.cmu.edu/~quake/triangle.node.html), a [.ele](https://www.cs.cmu.edu/~quake/triangle.node.html), a [.edge](https://www.cs.cmu.edu/~quake/triangle.node.html) and a [.neigh](https://www.cs.cmu.edu/~quake/triangle.node.html) file containing a refined Delaunay triangulation of the input poly. The exterior will be removed but not any holes within.

Usage:
```
triangulate_poly <input.poly> <min_angle>
```

`min_angle` specifies the minimum angles triangles in the triangulation should have.

The resulting triangulation can be plottet using the `plot_triangulation.py` Python script.

## Credits

This repository as well as its submodules use [Eigen](http://eigen.tuxfamily.org/index.php?title=Main_Page), a free C++ template library for linear algebra.
