function previewImage(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            document.getElementById('preview').src = e.target.result;　
            document.getElementById('preview').style.height = "500px";
        }
        
        reader.readAsDataURL(input.files[0]);
    }
}