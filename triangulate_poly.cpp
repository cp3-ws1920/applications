#include "triangulator.hpp"

#include <vector>
#include <fstream>
#include <iostream>

using namespace Triangulator;

int main(int argc, char *argv[]) {
    if (argc != 3) {
        std::cout << "Usage: " << argv[0] << " <input_file> <min_angle>" << std::endl;
    }
    float min_angle = std::stof((std::string)argv[2]);
    std::string fname = (std::string)argv[1];
    std::string iname = fname;
    iname.append(".poly");
    std::ifstream infile(iname, std::ifstream::in);
    if (!infile) {
        std::cout << "Could not open file " << iname << "!" << std::endl;
        return -1;
    }
    std::vector<Vertex *> poly;
    int num_vertices, dim, num_attrib, num_b_markers;
    infile >> num_vertices >> dim >> num_attrib >> num_b_markers;
    poly.resize(num_vertices);
    for (int i = 0; i < num_vertices; ++i) {
        float idx, x, y, attr;
        infile >> idx >> x >> y;
        for (int k = 0; k < num_attrib; ++k) {
            infile >> attr;
        }
        poly[i] = new Vertex(Eigen::Vector2f(x, y));
    }

    int num_segments;
    infile >> num_segments >> num_b_markers;
    std::cout << num_segments << std::endl;
    std::vector<Edge> segments;
    segments.resize(num_segments);
    for (int i = 0; i < num_segments; ++i) {
        int idx, orig, dest;
        infile >> idx >> orig >> dest;
        segments[i] = Edge(*poly[orig-1], *poly[dest-1]);
    }

    std::cout << "Set " << num_vertices << " vertices and " << num_segments << " segments." << std::endl;

    Delaunay2D delaunay;
    delaunay.vertices = poly;
    delaunay.segments = segments;
    delaunay.RefineRupperts(min_angle);
    delaunay.ToFile(fname);
}