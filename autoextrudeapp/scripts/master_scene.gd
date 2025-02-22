extends Node

@onready var file_dialog = FileDialog.new()
@onready var upload_button = $TextureButton  # Adjust path if needed
@onready var background = $Background  # Adjust path if needed

func _ready():
	add_child(file_dialog)  # Add FileDialog to the scene
	file_dialog.file_mode = FileDialog.FILE_MODE_OPEN_FILE
	file_dialog.access = FileDialog.ACCESS_FILESYSTEM

	# Only allow SVG, PNG, and JPG files
	file_dialog.filters = ["*.svg ; SVG Files", "*.png ; PNG Images", "*.jpg ; JPEG Images", "*.jpeg ; JPEG Images"]

	file_dialog.size = Vector2(800, 600)  # Set a larger size
	file_dialog.connect("file_selected", _on_file_selected)
	upload_button.connect("pressed", _on_upload_pressed)

func _on_upload_pressed():
	file_dialog.popup_centered_ratio(0.8)  # Open the file dialog (80% of screen size)

func _on_file_selected(path):
	var texture = load(path)  # Load selected image as texture
	if texture is Texture2D:
		background.texture = texture  # Set the new texture to the background
		print("Blueprint uploaded successfully: " + path)
	else:
		print("Invalid file selected!")
