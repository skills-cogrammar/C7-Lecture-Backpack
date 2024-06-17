import { Link, Outlet } from "react-router-dom";
import { useState, useEffect } from "react";
const Nested = () => {
  const [products, setProducts] = useState([]);

  const fetchProducts = async () => {
    const response = await fetch("https://fakestoreapi.com/products");
    const data = await response.json();
    console.log(data);
    setProducts(data);
  };

  useEffect(() => {
    fetchProducts();
  }, []);
  return (
    <section className="">
      <div className="flex w-full">
        <div className="w-1/2">
          {products.map((product) => {
            return (
              <div key={product.id}>
                <Link to={`/nested/${product.id}`} state={product}>{product.title}</Link>
              </div>
            );
          })}
        </div>
        <Outlet/>
      </div>
    </section>
  );
};

export default Nested;
