async function getPosts() {
  try {
    const response = await fetch("https://jsonplaceholder.typicode.com/posts");
    const blogs = await response.json();

    blogs.forEach((blog) => {
      console.log(blog);
    });
  } catch (err) {
    console.log(err);
  }
}

getPosts();

const createPost = async () => {
  const postData = {
    title: "Beverly Hills Cop 4",
    body: "This new installment in the BHC franchise will be landing on your screens soon.",
    userId: 100,
  };

  const response = await fetch("https://jsonplaceholder.typicode.com/posts", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(postData),
  });

  const data = await response.json();
  console.log("New post created:", data);
};

// createPost();

const getPost = async (postId) => {
  const response = await fetch(
    `https://jsonplaceholder.typicode.com/posts/${postId}`
  );
  const data = await response.json();
  console.log("Post retrieved:", data);
};

// getPost(1);

const updatePost = async (postId) => {
  const updateData = {
    title: "Updated Post Title",
    body: "This is the updated body of the post.",
    userId: 1,
  };

  const response = await fetch(
    `https://jsonplaceholder.typicode.com/posts/${postId}`,
    {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(updateData),
    }
  );

  const data = await response.json();
  console.log("Post updated:", data);
};

// updatePost(1);

const deletePost = async (postId) => {
  const response = await fetch(
    `https://jsonplaceholder.typicode.com/posts/${postId}`,
    {
      method: "DELETE",
    }
  );

  if (response.ok) {
    console.log("Post deleted successfully");
  } else {
    console.error("Failed to delete post");
  }
};

// deletePost(2);
