const markCompleteButtons = document.querySelectorAll("#mark-complete");
const deleteButtons = document.querySelectorAll("#delete-todo");


markCompleteButtons.forEach(button => {
  button.addEventListener("click", async () => {
    alert("Button clicked")
    const itemId = button.getAttribute("item-id");
    try {
      const response = await fetch(`/mark-complete/${itemId}`, {
        method: "POST",
      });
      if (!response.ok) {
        throw new Error(`Error marking item complete: ${response.statusText}`);
      }
      button.parentElement.remove()
      console.log("Item marked complete successfully!");
    } catch (error) {
      console.error("Error marking item complete:", error);
    }
  });
});


deleteButtons.forEach(button => {
  button.addEventListener("click", async () => {
    const itemId = button.getAttribute("item-id");
    try {
      const response = await fetch(`/delete-todo/${itemId}`, {
        method: "DELETE",
      });
      if (!response.ok) {
        throw new Error(`Error deleting item: ${response.statusText}`);
      }
      button.parentElement.remove()
      console.log("Item deleted successfully!");
    } catch (error) {
      console.error("Error deleting item:", error);
    }
  });
})