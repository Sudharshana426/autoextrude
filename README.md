# AutoExtrude

**Automated 2D to 3D Building Model Conversion Tool**

AutoExtrude is an open-source tool designed to automatically convert 2D floor plans into precise 3D building models. It leverages advanced image processing, vector analysis, and procedural mesh generation using the Godot Engine.

## Key Features

### 1. **Automated Wall Detection**
- **How it works:** Utilizes edge detection and vector analysis to extract wall structures from input images or vectors.
- **Algorithm:** Identifies walls based on contrast, thickness, and patterns in the input data.
- **Benefits:** Reduces manual effort by automatically detecting walls without requiring user intervention.

### 2. **Procedural Extrusion**
- **How it works:** Uses GDScript for dynamic mesh creation based on extracted wall dimensions.
- **Benefits:** Ensures precise scaling while maintaining model integrity.

### 3. **Shader-Based Material System**
- **How it works:** Custom shaders apply textures dynamically as users interact with the model.
- **Benefits:** Enhances visualization capabilities by allowing instant material changes.

### 4. **Optimized with GDScript**
- **How it works:** Leverages Godot’s scripting engine for optimized performance during complex geometric operations.
- **Benefits:** Maintains smooth performance even with large-scale models.

## Future Enhancements
- ✅ **Procedural Object Placement** – Automatically insert doors/windows based on predefined architectural rules.
- ✅ **Bézier Curve Lofting** – Support curved surfaces for more complex geometries.
- ✅ **GLTF/OBJ Export** – Improve compatibility with software like Blender, Unity, and Unreal Engine.
- ✅ **AI-Based Floor Plan Analysis** – Leverage machine learning for smarter room and wall detection.

## Problem Statement
Traditional architectural visualization tools require manual and time-consuming processes for creating 3D models from floor plans. This can be tedious for architects, designers, and developers who need quick visualizations.

### How AutoExtrude Solves This:
- **Drastically reduces modeling time** from hours to minutes through automation.
- **Eliminates expertise requirements** with a user-friendly interface that simplifies the process.

### Why AutoExtrude?
- **Reduces Modeling Time:** Automation significantly reduces manual labor, increasing productivity.
- **No Expertise Required:** The intuitive interface ensures anyone can use it without needing extensive knowledge of complex modeling software.
- **Accelerates Workflows:** Rapid visualization features enhance decision-making processes early in development cycles, saving resources and preventing costly mistakes.

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
1. Load a **floor plan image/vector file**.
2. Click **"Generate 3D Model"** to initiate the automated conversion process.

## License
This project is licensed under the **MIT License**.

## Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests.

## Contact
For any queries or feature requests, reach out via GitHub Issues.

---

*AutoExtrude: Automating 2D to 3D transformations with precision and ease.*
