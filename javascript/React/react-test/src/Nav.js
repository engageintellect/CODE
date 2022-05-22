import "./App.css";


function Nav() {
  return (
    <div className="container-fullwidth pt-3 d-flex justify-content-center gap-5">
      <a href="/" className="navbar_link">
        HOME
      </a>
      <a href="/about" className="navbar_link">
        ABOUT
      </a>
      <a href="/products" className="navbar_link">
        PRODUCTS
      </a>
      <a href="/contact" className="navbar_link">
        CONTACT
      </a>
      <a href="/news" className="navbar_link">
        NEWS
      </a>
      <a href="https://github.com/jc9361" className="navbar_link">
        GITHUB
      </a>
    </div>
  );
}

export default Nav;
