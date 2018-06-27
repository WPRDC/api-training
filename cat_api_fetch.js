// URL: https://beta.observablehq.com/@saylorsd/cat-api
// Title: Cat API
// Author: Steven Saylor (@saylorsd)
// Version: 189
// Runtime version: 1

const m0 = {
  id: "aef306c5255914f4@189",
  variables: [
    {
      inputs: ["md"],
      value: (function(md){return(
md`# Cat API
### But this time with fetch!`
)})
    },
    {
      name: "baseURL",
      value: (function(){return(
"https://thecatapi.com/"
)})
    },
    {
      name: "endpoint",
      value: (function(){return(
"api/images/get"
)})
    },
    {
      name: "requestURL",
      inputs: ["baseURL","endpoint"],
      value: (function(baseURL,endpoint){return(
baseURL + endpoint
)})
    },
    {
      name: "myBlob",
      inputs: ["requestURL"],
      value: (async function(requestURL){return(
await fetch(requestURL)
  .then(data => data.blob())
  .then(blob => blob)
)})
    },
    {
      inputs: ["myBlob"],
      value: (function(myBlob)
{
  let image = new Image();
  image.src = window.webkitURL.createObjectURL( myBlob);
  return image
}
)
    },
    {
      inputs: ["requestURL"],
      value: (async function(requestURL)
{
  let newBlob = await fetch(requestURL)
                .then(data => data.blob())
                .then(blob => blob);
  let image = new Image;
  image.src = image.src = window.URL.createObjectURL(newBlob);
  return image
}
)
    },
    {
      name: "spaceURL",
      inputs: ["requestURL"],
      value: (function(requestURL){return(
requestURL + "?category=space&size=large"
)})
    },
    {
      name: "categoryURL",
      inputs: ["spaceURL"],
      value: (async function(spaceURL)
{
  let spaceBlob = await fetch(spaceURL)
            .then(data => data.blob());
  let image = new Image();
  image.src = window.webkitURL.createObjectURL(spaceBlob);
  return image
}
)
    }
  ]
};

const notebook = {
  id: "aef306c5255914f4@189",
  modules: [m0]
};

export default notebook;