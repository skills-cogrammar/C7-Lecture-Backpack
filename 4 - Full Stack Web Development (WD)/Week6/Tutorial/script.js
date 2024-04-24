const apiUrl = 'https://jsonplaceholder.typicode.com/posts';

let postList = document.getElementById('postList');

// Function to fetch data from the api and list items on the page.
async function getPosts(){
    try{
        let response = await fetch(apiUrl);
        let data = await response.json();
        console.log(data);
        data.forEach(blog => {
            let listItem = document.createElement('li');
    
            //Blog title
            let h3 = document.createElement('h3');
            h3.innerHTML = blog.title;
            listItem.appendChild(h3);
    
            //Blog content
            let content = document.createElement('p');
            content.innerHTML = blog.body;
            listItem.appendChild(content);
    
            //Delete button
            let deleteBtn = document.createElement('button');
            deleteBtn.innerHTML = "Delete";
            deleteBtn.addEventListener("click", function(){
                deletePost(blog.id);
            });

            listItem.appendChild(deleteBtn);

            //Edit button
            let editBtn = document.createElement('button');
            editBtn.innerHTML = "Edit";
            editBtn.addEventListener("click", function(){
                //Handle edit click
                editPost(blog.id, blog.title, blog.body);
            });

            listItem.appendChild(editBtn);

            postList.appendChild(listItem);
            
        });
    }catch(err){
        console.log(err);
    }

    
}

async function deletePost(postId){
    try{
        let response = await fetch(`${apiUrl}/${postId}`, {
            method: "DELETE"
        })
    
        if(response.ok){
            alert("Deletion was succesful.");
        }
        getPosts();
    }catch(err){
        console.log(err);
    }
}

async function addPost(title, content){

    try{
        let response = await fetch(apiUrl, {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                title: title,
                body: content,
            }) 
        })
    
        let data = await response.json();
        alert(`New post successfully created: ${JSON.stringify(data)}`);
        getPosts();
    }catch(err){
        console.log(err);
    }

}

function editPost(postId, title, content){
    let newTitle = prompt("Enter the new title:", title);
    let newBody = prompt("Enter the new content:", content);
    if(newTitle && newBody){
        updatePost(postId, newTitle, newBody);
    }
}

async function updatePost(postId, title, content){
    try{
        let response = await fetch(`${apiUrl}/${postId}`, {
            method: "PUT",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                title: title,
                body: content,
            }) 
        })
    
        let data = await response.json();
        alert(`Updated successfully: ${JSON.stringify(data)}`);
        getPosts();
    }catch(err){
        console.log(err);
    }
}

document.getElementById("addpostbtn").addEventListener('click', e => {
    e.preventDefault();
    let title = document.getElementById('title').value;
    let content =  document.getElementById('body').value;
    addPost(title, content);
});

getPosts();