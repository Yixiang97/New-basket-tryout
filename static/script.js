document.addEventListener("DOMContentLoaded", async () => {
  // Fetch personnel list
  const response = await fetch("/api/personnel");
  const personnel = await response.json();

  const nameDropdown = document.getElementById("name");
  personnel.forEach(person => {
    const option = document.createElement("option");
    option.value = person.name;
    option.textContent = person.name;
    nameDropdown.appendChild(option);
  });

  // Handle form submission
  document.getElementById("leaveForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    const data = {
      name: nameDropdown.value,
      start: document.getElementById("start").value,
      end: document.getElementById("end").value,
      reason: document.getElementById("reason").value
    };

    const res = await fetch("/submit-leave", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data)
    });

    const result = await res.json();
    document.getElementById("status").textContent = result.message;
    document.getElementById("leaveForm").reset();
  });
});
