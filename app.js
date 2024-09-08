let data = [];

fetch("dic_data.json")
  .then((response) => response.json())
  .then((jsonData) => {
    data = jsonData;
  })
  .catch((error) => console.error("Error loading JSON data:", error));

function searchWord() {
  const input = document.getElementById("search-input").value.trim();
  const resultDiv = document.getElementById("result");
  const result = data.find((item) => item["Từ vựng"] === input);

  if (result) {
    resultDiv.textContent = `${result["Từ vựng"]}: ${result["Nghĩa"]}`;
  } else {
    resultDiv.textContent = "Không tìm thấy từ này.";
  }
}
