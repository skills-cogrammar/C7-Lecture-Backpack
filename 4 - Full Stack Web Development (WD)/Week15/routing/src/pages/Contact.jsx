import Navbar from "../components/NavBar";
import { useLocation, useNavigation, useParams } from "react-router-dom";

const Contact = () => {
  const { contactId } = useParams();
  const character = useLocation().state;
  const navigation = useNavigation();
  console.log(navigation.state)
  return (
    <>
      {navigation.state === "loading" ? (
        <h1>Loading</h1>
      ) : (
        <>
          <h1>{character.name}</h1>

          <div className="w-[100px] h-[100px]">
            <img
              src={character.image}
              alt="character"
              className="w-full h-full object-contain"
            />
          </div>
        </>
      )}
    </>
  );
};

export default Contact;
