// FABLE - SIH26152 frontend logic
// Owner: Adiya (Research/UI-UX + Visualization)
//
// Step 1: confirm we can send a file to the backend and see a response.
// Later: replace the raw JSON dump below with real Plotly charts.

const BACKEND_URL = "http://127.0.0.1:8000";

const fileInput = document.getElementById("fileInput");
const uploadBtn = document.getElementById("uploadBtn");
const statusEl = document.getElementById("status");
const resultsOutput = document.getElementById("resultsOutput");

uploadBtn.addEventListener("click", async () => {
  const file = fileInput.files[0];
  if (!file) {
    statusEl.textContent = "Please choose a CSV file first.";
    return;
  }

  statusEl.textContent = "Uploading...";

  const formData = new FormData();
  formData.append("file", file);

  try {
    const response = await fetch(`${BACKEND_URL}/upload`, {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      throw new Error(`Server responded with ${response.status}`);
    }

    const data = await response.json();
    statusEl.textContent = "Done.";

    // Placeholder: show raw JSON until real chart rendering is built.
    resultsOutput.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
  } catch (err) {
    statusEl.textContent = `Error: ${err.message}`;
  }
});
