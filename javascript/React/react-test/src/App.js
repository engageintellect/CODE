// -------------------------------------------------
//  MAIN APP
// -------------------------------------------------


// ------------------------
//  IMPORTS
// ------------------------
import React, { useState } from "react";
import "./App.css";
import Nav from "./Nav.js";


const App = (props) => {
// ------------------------
//  STATE
// ------------------------
  const [title, setTitle] = useState("title");
  const [footer, setFooter] = useState("title");
  const [subtext, setSubtext] = useState("subtext");
  const [card1, setCard1] = useState("card1");
  const [card2, setCard2] = useState("card2");
  const [card3, setCard3] = useState("card3");
  const [card4, setCard4] = useState("card4");
  const [clickhere, setClickhere] = useState("CLICK");
  const [stat, setStat] = useState("col alert alert-danger");
    

// ------------------------
//  RETURN
// ------------------------
  return (
    <React.Fragment>
      <Nav />

      <div className="container-fullwidth mx-auto">
        <section>
          <div className="jumbotron align-center header pt-5">
            <div className="container">
              <h1 className="display-1">{title}</h1>
              <p className="lead">{subtext}</p>
              <button
                onClick={() => {
                    setTitle("This is My New Title");
                    setSubtext("this is some cliche subtext");
                    setStat("col alert alert-info");
                    setCard1("Info: Some news");
                    setCard2("Info: Some more news");
                    setCard3("Info: Some more more news");
                    setCard4("Info: Some more more news");
                        setClickhere("CLICK");
                    }}
                    className="btn btn-primary shadow">
                {clickhere}
              </button>
            </div>
          </div>
        </section>

        <section>
          <div className="container row pt-5 mx-auto gap-2">
            <h2 className={stat}>{card1}</h2>
            <h2 className={stat}>{card2}</h2>
            <h2 className={stat}>{card3}</h2>
            <h2 className={stat}>{card4}</h2>
          </div>

          <div className="container">
            <div className="row pt-5 pb-5">
              <p className="col">
                hello world, this is the end. hi hey hello howdy. hello world,
                this is the end. hi hey hello howdy. hello world, this is the
                end. hi hey hello howdy. hello world, this is the end. hi hey
                hello howdy. hello world, this is the end. hi hey hello howdy.
                hello world, this is the end. hi hey hello howdy. hello world,
                this is the end. hi hey hello howdy. hello world, this is the
                end. hi hey hello howdy. hello world, this is the end. hi hey
                hello howdy. hello world, this is the end. hi hey hello howdy.
                hello world, this is the end. hi hey hello howdy. hello world,
                this is the end. hi hey hello howdy. hello world, this is the
                end. hi hey hello howdy. hello world, this is the end. hi hey
                hello howdy.
              </p>

              <p className="col">
                hello world, this is the end. hi hey hello howdy. hello world,
                this is the end. hi hey hello howdy. hello world, this is the
                end. hi hey hello howdy. hello world, this is the end. hi hey
                hello howdy. hello world, this is the end. hi hey hello howdy.
                hello world, this is the end. hi hey hello howdy.
              </p>
            </div>
          </div>

          <div className="container-fullwidth mx-auto">
            <section>
              <div className="jumbotron align-center header pt-5">
                <div className="container">
                  <h1 className="display-1">{footer}</h1>
                  <p className="lead">{subtext}</p>
                  <button
                    onClick={() => {
                        setStat("col alert alert-danger");
                        setCard1("this is a danger alert");
                        setCard2("this is a danger alert");
                        setCard3("this is a danger alert");
                        setCard4("this is a danger alert");
                        setFooter("This is a Footer");
                        setClickhere("My Button");
 
                    }}
                    className="btn btn-primary shadow">
                    {clickhere}
                  </button>
                </div>
              </div>
            </section>
          </div>
        </section>
      </div>
    </React.Fragment>
  );
};

export default App;
