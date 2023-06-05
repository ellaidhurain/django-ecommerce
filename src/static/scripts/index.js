
// const e = React.createElement;
const useState = React.useState;

function App(props) {
  const [count, setRandomCount] = useState(function generateRandomInteger() {
    return Math.floor(Math.random() * 100);
  });

  function clickHandler(e) {
    setRandomCount(Math.floor(Math.random() * 100));
  }


  // const list = ['a','b','c']

  return (
    <div style={{ margin: "auto", width: 100, display: "block" }}>
      {/* {list.map((data)=>(
        <p>{data}</p>
      ))} */}
      <h1> {count} </h1>
      <p>
        <button onClick={clickHandler}> Click </button>
      </p>
    </div>
  );
}

const domContainer = document.querySelector("#root");

const root = ReactDOM.createRoot(domContainer); // createRoot(container!) if you use TypeScript
root.render(<App tab="home" />);

