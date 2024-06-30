import { gql, useMutation } from "@apollo/client";
import { useState } from "react";

const CREATE_EMPLOYEE = gql`
  mutation CreateEmployee(
    $name: String
    $email: String
    $role: String
    $lineManager: String
  ) {
    create(name: $name, email: $email, role: $role, lineManager: $lineManager) {
      email
      lineManager
      name
      role
    }
  }
`;

const Update = () => {
  const [create, { data, error, loading }] = useMutation(CREATE_EMPLOYEE);
  const [email, setEmail] = useState("");
  const [name, setName] = useState("");
  const [role, setRole] = useState("");
  const [lineManager, setLineManager] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    create({
      variables: {
        email,
        name,
        role,
        lineManager,
      },
    });
  };

  if (loading) return <h1>Submitting...</h1>;
  if (error) return <h1>Error in submitting</h1>;

  console.log(data)

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" placeholder="Name" onChange={(e) => setName(e.target.value)} />
      <input type="text" placeholder="Email" onChange={(e) => setEmail(e.target.value)} />
      <input type="text" placeholder="Role" onChange={(e) => setRole(e.target.value)} />
      <input type="text" placeholder="Line Manager" onChange={(e) => setLineManager(e.target.value)} />
      <button type="submit">Submit</button>
    </form>
  );
};

export default Update;
