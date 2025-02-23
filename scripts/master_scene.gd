#extends Node2D
#
#@onready var file_dialog = FileDialog.new()
#@onready var sprite = $Sprite  # Sprite2D for displaying the uploaded image
#@onready var upload_button = $Sprite/Upload  # Upload button
#@onready var python_script_path = "res://wall_extrusion.py"  # Ensure correct path
#
#func _ready():
	## Ensure UI elements are correctly assigned
	#if not upload_button:
		#print("ERROR: Upload button is NULL! Check scene structure.")
		#return
#
	#if not sprite:
		#print("ERROR: Sprite is NULL! Check scene structure.")
		#return
#
	## Configure FileDialog for selecting image files
	#add_child(file_dialog)  # Attach FileDialog to the scene
	#file_dialog.file_mode = FileDialog.FILE_MODE_OPEN_FILE
	#file_dialog.access = FileDialog.ACCESS_FILESYSTEM
	#file_dialog.filters = ["*.svg ; SVG Files", "*.png ; PNG Images", "*.jpg ; JPEG Images", "*.jpeg ; JPEG Images"]
	#file_dialog.size = Vector2(800, 600)  # Set a larger window size
	#file_dialog.connect("file_selected", _on_file_selected)
#
	## Connect button to function
	#var result = upload_button.connect("pressed", _on_upload_pressed)
	#if result != OK:
		#print("ERROR: Failed to connect upload button!")
#
#func _on_upload_pressed():
	#"""Opens the file dialog when the upload button is pressed."""
	#file_dialog.popup_centered_ratio(0.8)
#
#func _on_file_selected(path):
	#"""Handles file selection, updates the sprite, and runs the Python script."""
	#_update_sprite(path)  # Load and display the selected image
	#_run_python_script(path)  # Execute the Python script for wall extrusion
#
#func _update_sprite(path):
	#var img = Image.new()
	#var gr = img.load(path)
	#if gr == OK:
		#var texture = ImageTexture.new()
		#texture.create_from_image(img)
		#sprite.texture = texture
		#print("Blueprint uploaded successfully: " + path)
	#else:
		#print("Invalid file selected!")
#
#func _run_python_script(path):
	#"""Executes the Python script to generate a 3D wall model."""
	#var python_script_path = ProjectSettings.globalize_path("res://scripts/wall_extrusion.py")
#
	#var result = []
	#var status = OS.execute("/home/navin-lakshh/miniconda3/envs/ollama/bin/python3.12", [python_script_path, path], result, true)
#
	#if status == 0:
		#print("✅ 3D Wall Model Generated Successfully!")
	#else:
		#print("❌ Error Generating 3D Wall Model! Output:", result)
#


extends Node2D

@onready var file_dialog = FileDialog.new()
@onready var sprite = $Sprite  # Displays the uploaded image
@onready var upload_button = $Sprite/Upload  # Upload button
@onready var python_script_path = "res://wall_extrusion.py"  # Path to script

@onready var background = null  # Background sprite (assigned dynamically)
@onready var height_dialog = AcceptDialog.new()
@onready var height_line_edit = LineEdit.new()

var uploaded_file_path = ""

func _ready():
	# Ensure UI elements are correctly assigned
	if not upload_button:
		print("ERROR: Upload button is NULL! Check scene structure.")
		return

	if not sprite:
		print("ERROR: Sprite is NULL! Check scene structure.")
		return

	# Ensure the background exists and is assigned
	if has_node("Background"):
		background = $Background
		background.z_index = -2  # Push background behind everything
	else:
		print("WARNING: Background not found in the scene! Make sure it's named 'Background'.")

	sprite.z_index = 1  # Ensure uploaded image stays on top

	# Configure FileDialog for selecting image files
	add_child(file_dialog)
	file_dialog.file_mode = FileDialog.FILE_MODE_OPEN_FILE
	file_dialog.access = FileDialog.ACCESS_FILESYSTEM
	file_dialog.filters = ["*.svg ; SVG Files", "*.png ; PNG Images", "*.jpg ; JPEG Images", "*.jpeg ; JPEG Images"]
	file_dialog.connect("file_selected", _on_file_selected)

	# Connect Upload Button
	var result = upload_button.connect("pressed", _on_upload_pressed)
	if result != OK:
		print("ERROR: Failed to connect upload button!")

	# Create User Input Dialog (for height)
	height_dialog.dialog_text = "Enter the height:"
	height_dialog.ok_button_text = "Apply"
	height_dialog.size = Vector2(300, 150)
	
	# Configure LineEdit for height input
	height_line_edit.placeholder_text = "Enter height (e.g., 2.5)"
	height_line_edit.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	height_dialog.add_child(height_line_edit)
	
	# Connect Dialog Confirmation
	height_dialog.connect("confirmed", _on_height_entered)
	
	add_child(height_dialog)  # Add to the scene

func _on_upload_pressed():
	"""Opens the file dialog when the upload button is pressed."""
	file_dialog.popup_centered_ratio(0.8)

func _on_file_selected(path):
	"""Handles file selection, updates the sprite, and asks for height input."""
	uploaded_file_path = path  # Store the uploaded file path
	_update_sprite(path)  # Load and display the selected image
	height_dialog.popup_centered()  # Ask for height after image selection

func _update_sprite(path):
	"""Loads and sets the selected image as texture on the sprite."""
	#func _update_sprite(path):
	var img = Image.new()
	var gr = img.load(path)
	if gr == OK:
		var texture = ImageTexture.new()
		texture.create_from_image(img)
		sprite.texture = texture
		print("✅ Blueprint uploaded successfully: " + path)
		if background:
			background.z_index = -2  # Ensure it's still in the background
		else:
			print("WARNING: Background is NULL. Check if it's in the scene.")
	#var texture = load(path)
	#if texture is Texture2D:
		#sprite.texture = texture
		#print(" Blueprint uploaded successfully: " + path)

		# Re-apply background to prevent it from disappearing
	else:
		print("❌ Invalid file selected!")

func _on_height_entered():
	"""Handles the height input and proceeds to the next step."""
	var user_height = height_line_edit.text.to_float()
	if user_height > 0 and uploaded_file_path != "":
		print("User entered height:", user_height)
		_run_python_script(uploaded_file_path, user_height)  # Pass both path and height
	else:
		print("❌ Invalid height or file path! Please enter valid inputs.")

func _run_python_script(image_path, height):
	"""Executes the Python script with both the image path and height value."""
	var global_python_script_path = ProjectSettings.globalize_path("res://scripts/wall_extrusion.py")
	var global_image_path = ProjectSettings.globalize_path(image_path)

	var result = []
	var status = OS.execute("/home/navin-lakshh/miniconda3/envs/ollama/bin/python3.12", [global_python_script_path, global_image_path, str(height)], result, true)

	if status == 0:
		print("✅ 3D Wall Model Generated Successfully!")
	else:
		print("❌ Error Generating 3D Wall Model! Output:", result)
