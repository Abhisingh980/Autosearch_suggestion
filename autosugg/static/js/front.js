function showSuggestions(query) {
  const suggestionsList = document.getElementById("suggestions-list");
  suggestionsList.innerHTML = "";

  if (query.trim() === "") return;

  const suggestions = [
    "JavaScript",
    "HTML",
    "CSS",
    "Python",
    "Django",
    "React",
    "Vue.js",
    "Node.js",
    "Elasticsearch",
  ];

  const filteredSuggestions = suggestions.filter((item) =>
    item.toLowerCase().includes(query.toLowerCase()),
  );

  filteredSuggestions.forEach((suggestion) => {
    const li = document.createElement("li");
    li.textContent = suggestion;
    li.onclick = () => {
      document.getElementById("search-box").value = suggestion;
      suggestionsList.innerHTML = "";
    };
    suggestionsList.appendChild(li);
  });
}
