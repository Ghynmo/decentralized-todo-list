from algopy import ARC4Contract, String, UInt64, arc4, GlobalState, BoxMap


class TodoApp(ARC4Contract):
    """
    A simple Todo application smart contract for Algorand.
    Allows users to create, complete, and view their todos.
    """
    
    def __init__(self) -> None:
        # Counter to track total number of todos created
        self.todo_counter = GlobalState(UInt64(0))
        # Store todos using BoxMap: todo_id -> todo_text
        self.todos = BoxMap(arc4.UInt64, arc4.String)
        # Store completion status: todo_id -> is_completed
        self.completed = BoxMap(arc4.UInt64, arc4.Bool)
    
    @arc4.abimethod()
    def create_todo(self, task: arc4.String) -> arc4.UInt64:
        """
        Create a new todo item.
        Returns the ID of the created todo.
        """
        # Increment the counter to get new todo ID
        current_id = self.todo_counter.value
        new_id = current_id + UInt64(1)
        self.todo_counter.value = new_id
        
        # Store the todo task
        todo_id = arc4.UInt64(new_id)
        self.todos[todo_id] = task
        self.completed[todo_id] = arc4.Bool(False)
        
        return todo_id
    
    @arc4.abimethod()
    def complete_todo(self, todo_id: arc4.UInt64) -> arc4.String:
        """
        Mark a todo as completed.
        Returns a success message.
        """
        # Check if todo exists
        if todo_id not in self.todos:
            return arc4.String("Todo not found")
        
        # Mark as completed
        self.completed[todo_id] = arc4.Bool(True)
        
        return arc4.String("Todo marked as completed!")
    
    @arc4.abimethod()
    def get_todo(self, todo_id: arc4.UInt64) -> arc4.String:
        """
        Get a specific todo by its ID.
        Returns the todo text.
        """
        if todo_id not in self.todos:
            return arc4.String("Todo not found")
        
        return self.todos[todo_id]
    
    @arc4.abimethod()
    def is_completed(self, todo_id: arc4.UInt64) -> arc4.Bool:
        """
        Check if a todo is completed.
        Returns True if completed, False otherwise.
        """
        if todo_id not in self.completed:
            return arc4.Bool(False)
        
        return self.completed[todo_id]
    
    @arc4.abimethod()
    def get_total_todos(self) -> arc4.UInt64:
        """
        Get the total number of todos created.
        """
        return arc4.UInt64(self.todo_counter.value)
    
    @arc4.abimethod()
    def delete_todo(self, todo_id: arc4.UInt64) -> arc4.String:
        """
        Delete a todo item.
        Returns a success message.
        """
        if todo_id not in self.todos:
            return arc4.String("Todo not found")
        
        # Delete from both storage boxes
        del self.todos[todo_id]
        del self.completed[todo_id]
        
        return arc4.String("Todo deleted successfully!")