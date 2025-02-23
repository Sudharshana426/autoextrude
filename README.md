# AutoExtrude

**Automated 2D to 3D Building Model Conversion Tool**

AutoExtrude is an open-source tool designed to automatically convert 2D floor plans into precise 3D building models. It leverages advanced image processing, vector analysis, and procedural mesh generation using the Godot Engine.

##Why Godot and Why Autoextrude?
Traditional architectural visualization tools require manual and time-consuming processes for creating 3D models from floor plans. This can be tedious for architects, designers, and developers who need quick visualizations.

- **Reduces Modeling Time:** Automation significantly reduces manual labor, increasing productivity.
- **No Expertise Required:** The intuitive interface ensures anyone can use it without needing extensive knowledge of complex modeling software.
- **Accelerates Workflows:** Rapid visualization features enhance decision-making processes early in development cycles, saving resources and preventing costly mistakes.

## Key Processes involved

### 1. **Automated Edge Detection**
- **How it works:** Converts the image to grayscale and uses Guassian blur to remove unneccesaary noises like text etc. on the blueprint maintaining the structure . We use Edge canny method to highlight the sharp edge walls.
- **Algorithm:** Identifies walls based on contrast, thickness, and patterns in the input data.
- **Benefits:** Reduces manual effort by automatically detecting walls without requiring user intervention.

### 2. **Procedural Extrusion**
After detecting the edges the most important step is to extract the wall boundaries and represent them in vector form of data. 
- **How it works:** Extracts continous wall outlines from the edge and stores walls as line segments in vector format.
- **Benefits:** Ensures precise scaling while maintaining model integrity and bridges the gap between image processing and 3D modeling.

### 3. **Mesh Generation**
The conversion of 2D to 3D takes place here. It provides visualization of building structure.
- **How it works:** Uses wall contours to define mesh vertices and create a triangular faces connecting these points.
- **Benefits:** Enables dynamic shape creation using procedural techniques.

### 4. **Extrusion**
- **How it works:** Giving depths to walls in 3D. 
It duplicates vertices from contour points, connect the bases and top using triangular faces and give out the final extruded 3D model.
- **Benefits:** Enhances visualization capabilities by allowing instant material changes.

## Future Enhancements
- ✅ **Procedural Object Placement** – Automatically insert doors/windows based on predefined architectural rules.
- ✅ **Bézier Curve Lofting** – Support curved surfaces for more complex geometries.
- ✅ **GLTF/OBJ Export** – Improve compatibility with software like Blender, Unity, and Unreal Engine.
- ✅ **AI-Based Floor Plan Analysis** – Leverage machine learning for smarter room and wall detection.


## How It Works
1. Click **"Upload Floor Plan"** to initiate the automated conversion process.
2. **Edge Detection & Vector Analysis:** Advanced algorithms identify walls based on contrast, thickness, and patterns.
3. **Procedural Extrusion:** Converts the detected walls into a full 3D model with real-time scaling.

## Tech Stack
1. **Godot Engine (4.x):** Used for real-time rendering and GDScript-based mesh generation.
2. **GDScript:** Lightweight yet high-performance language for procedural geometry manipulation.
3. **Image Processing Techniques:** Edge detection algorithms (e.g., Canny Edge Detection) for accurate boundary identification.
4. **Shader Programming:** Custom shaders for dynamic material application and UV mapping.

## Installation & Usage

### Prerequisites
- Install **Godot Engine** (version 4.x recommended).
- Clone this repository using the Git command-line tool or GitHub Desktop client:
  ```sh
  git clone https://github.com/your-github-account-name/autoextrude.git  
  cd autoextrude  
  ```
- Open the project in the Godot Editor environment.

### Usage Instructions
1. Load a **BluePrint of a building**.
2. Click **"Upload the bluePrint"** to initiate the automated conversion process.

## License
This project is licensed under the **MIT License**.

## Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests.

