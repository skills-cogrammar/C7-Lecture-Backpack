function UserIcon(username, logo) {
    const userIcon = document.createElement("div");    
    userIcon.classList.add("user-icon");
    userIcon.innerHTML = `
        <img src="${logo}" alt="${username} data-username="${username}">
    `;

    return userIcon;
}

export default UserIcon;