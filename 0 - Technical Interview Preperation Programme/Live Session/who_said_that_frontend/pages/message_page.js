import UserIcon from "../components/user_icon.js";

const users = [];

class User {
    constructor(username, logo) {
        this.username = username;
        this.logo = logo;
        this.messages = [];
    }
}

function MessagePage() {
    const messagePage = document.createElement("main");
    messagePage.classList.add("message-page");

    const usersPanel = UsersPanel();
    
    messagePage.appendChild(usersPanel);

    return messagePage;
}

function UsersPanel() {
    const usersPanel = document.createElement("div");
    const usersContainer = document.createElement("div");
    usersContainer.classList.add("users-container");

    const addUsersButton = document.createElement("button");
    addUsersButton.innerHTML = "+";
    addUsersButton.id = "add-users-button";

    addUsersButton.addEventListener("click", () => {
        const username = prompt("Enter username:");
        const logo = prompt("Enter logo url:");

        if (username && logo) {
            const user = new User(username, logo);
            users.push(user);
            usersContainer.appendChild(UserIcon(user.username, user.logo));
        }
    })

    usersPanel.appendChild(usersContainer);
    usersPanel.appendChild(addUsersButton);

    return usersPanel;
}

function MessagePanel() {
    const messagePanel = document.createElement("div");
}

export default MessagePage;