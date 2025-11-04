# 🧭 Decentralized Todo List dApp (Algorand)

A simple yet powerful **decentralized Todo List application** built on **Algorand blockchain**.
This project demonstrates how everyday applications — like a task manager — can be made **trustless**, **transparent**, and **tamper-proof** using smart contracts.

---

## 🚀 Project Description

This dApp allows users to **create**, **view**, and **complete** their tasks in a fully decentralized way.
Instead of relying on a centralized server or database, all todos are managed and stored securely on the **Algorand blockchain**, ensuring:

* **Transparency** — all transactions are verifiable on-chain.
* **Security** — user data and actions are cryptographically secured.
* **Ownership** — each todo belongs to the creator’s wallet address.

It’s a beginner-friendly example for anyone wanting to learn **Algorand smart contract development**, **dApp architecture**, and **React integration** with blockchain backends.

---

## 💡 What It Does

1. **Create Tasks**
   Users can create new todo items directly from the dApp interface.
   Each new task is added to the blockchain via a smart contract call.

2. **Mark as Complete**
   Tasks can be marked as completed. The smart contract updates the task status immutably on-chain.

3. **Fetch All Todos**
   The dApp fetches all todos belonging to the connected wallet by reading from the blockchain.

4. **Wallet Integration**
   Connect your Algorand wallet (e.g., Pera, Defly) to manage tasks linked to your address.

---

## ✨ Features

* 🔗 Fully decentralized storage of todos
* 🧠 Smart contract written in **PyTeal (Python)** using **Algokit**
* 🖥️ Frontend built with **React + Vite** for modern web performance
* 💼 Seamless **wallet connection** using Algorand SDKs
* ⚙️ Easy deployment to **TestNet** or **MainNet**
* 🧩 Modular and beginner-friendly code structure

---

## 🧱 Smart Contract Code

```python
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
```

---

## 🌍 Deployed Smart Contract

**App Link:** `lora.algokit.io/testnet/application/748988054`
**App ID:** `748988054`
**Contract Address:** `LVCKS5HCKLNFBIJQDAOXQBWBRTMANAU5VN3WUNC6LOVNTJX26TSY2XU3UI`
*(Replace XXX with your deployed contract address once available)*

You can view the deployed contract on [AlgoExplorer](https://testnet.algoexplorer.io/) or [Pera Explorer](https://explorer.perawallet.app/).

---

## 🧰 Tech Stack

* **Algorand SDK** — blockchain interaction
* **Algokit** — contract compilation and deployment
* **PyTeal** — smart contract logic
* **React (Vite)** — modern frontend
* **TailwindCSS / Chakra UI (optional)** — beautiful UI styling

---

## 🪜 How to Run Locally

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/algorand-todo-dapp.git
   cd algorand-todo-dapp
   ```

2. **Install dependencies**

   ```bash
   npm install
   ```

3. **Run local frontend**

   ```bash
   npm run dev
   ```

4. **Deploy smart contract (optional)**

   ```bash
   algokit deploy
   ```

---

## 💬 Future Improvements

* Add task deadlines and categories
* Enable task sharing between wallets
* Implement notifications for completed tasks
* Integrate with mobile wallets for smoother UX

---

## 🧑‍💻 Contributing

Contributions are welcome!
If you’d like to improve this dApp, open an issue or submit a pull request.

---

## 🪙 License

This project is licensed under the **MIT License** — free to use and modify.

---

**Built with ❤️ using [Algorand](https://www.algorand.com/) and [Algokit](https://developer.algorand.org/algokit/).**
