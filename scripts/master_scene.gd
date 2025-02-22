extends Node2D

@onready var file_dialog = FileDialog.new()
@onready var sprite = $Sprite  # Sprite2D for displaying the uploaded image
@onready var upload_button = $Sprite/Upload  # Upload button
@onready var python_script_path = "res://wall_extrusion.py"  # Ensure correct path

func _ready():
	# Ensure UI elements are correctly assigned
	if not upload_button:
		print("ERROR: Upload button is NULL! Check scene structure.")
		return

	if not sprite:
		print("ERROR: Sprite is NULL! Check scene structure.")
		return

	# Configure FileDialog for selecting image files
	add_child(file_dialog)  # Attach FileDialog to the scene
	file_dialog.file_mode = FileDialog.FILE_MODE_OPEN_FILE
	file_dialog.access = FileDialog.ACCESS_FILESYSTEM
	file_dialog.filters = ["*.svg ; SVG Files", "*.png ; PNG Images", "*.jpg ; JPEG Images", "*.jpeg ; JPEG Images"]
	file_dialog.size = Vector2(800, 600)  # Set a larger window size
	file_dialog.connect("file_selected", _on_file_selected)

	# Connect button to function
	var result = upload_button.connect("pressed", _on_upload_pressed)
	if result != OK:
		print("ERROR: Failed to connect upload button!")

func _on_upload_pressed():
	"""Opens the file dialog when the upload button is pressed."""
	file_dialog.popup_centered_ratio(0.8)

func _on_file_selected(path):
	"""Handles file selection, updates the sprite, and runs the Python script."""
	_update_sprite(path)  # Load and display the selected image
	_run_python_script(path)  # Execute the Python script for wall extrusion

func _update_sprite(path):
	"""Loads and sets the selected image as texture on the sprite."""
	var texture = load(path)
	if texture is Texture2D:
		sprite.texture = texture
		print("Blueprint uploaded successfully: " + path)
	else:
		print("Invalid file selected!")

func _run_python_script(path):
	"""Executes the Python script to generate a 3D wall model."""
	var python_script_path = ProjectSettings.globalize_path("res://scripts/wall_extrusion.py")

	var result = []
	var status = OS.execute("python3", [python_script_path, path], result, true)

	if status == 0:
		print("✅ 3D Wall Model Generated Successfully!")
	else:
		print("❌ Error Generating 3D Wall Model! Output:", result)
