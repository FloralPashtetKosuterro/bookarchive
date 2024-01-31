

window.onload = () => {
    CKEDITOR.replace("part_content");
  };

  function sendText() {
    window.parent.postMessage(CKEDITOR.instances.part_content.getData(), "*");
  };


