// script.js

const suggestions = [
  "JavaScript",
  "HTML",
  "CSS",
  "Python",
  "Java",
  "Django",
  "React",
  "Vue.js",
  "Node.js",
  "Elasticsearch",
];

function showSuggestions(input) {
  const suggestionsList = document.getElementById("suggestions-list");
  suggestionsList.innerHTML = ""; // Clear existing suggestions

  if (!input) {
    suggestionsList.style.display = "none";
    return;
  }

  const filteredSuggestions = suggestions.filter((suggestion) =>
    suggestion.toLowerCase().startsWith(input.toLowerCase()),
  );

  if (filteredSuggestions.length > 0) {
    suggestionsList.style.display = "block";
    filteredSuggestions.forEach((suggestion) => {
      const li = document.createElement("li");
      li.textContent = suggestion;
      li.addEventListener("click", () => selectSuggestion(suggestion));
      suggestionsList.appendChild(li);
    });
  } else {
    suggestionsList.style.display = "none";
  }
}

function selectSuggestion(value) {
  document.getElementById("search-box").value = value;
  document.getElementById("suggestions-list").style.display = "none";
}
