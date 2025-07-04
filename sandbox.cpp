#include "ofMain.h"

class ofApp : public ofBaseApp {
public:
    ofMesh mesh;

    void setup() {
        // Create a rectangular mesh (quad)
        mesh.setMode(OF_PRIMITIVE_TRIANGLE_STRIP);

        // Define rectangle corners
        mesh.addVertex(glm::vec3(100, 100, 0)); // Top-left
        mesh.addVertex(glm::vec3(300, 100, 0)); // Top-right
        mesh.addVertex(glm::vec3(100, 300, 0)); // Bottom-left
        mesh.addVertex(glm::vec3(300, 300, 0)); // Bottom-right

        // Optionally add color
        mesh.addColor(ofColor::red);
        mesh.addColor(ofColor::green);
        mesh.addColor(ofColor::blue);
        mesh.addColor(ofColor::yellow);
    }

    void draw() {
        ofBackground(30);
        mesh.draw();
    }
};

//========================================================================
int main() {
    ofSetupOpenGL(640, 480, OF_WINDOW);
    ofRunApp(new ofApp());
}