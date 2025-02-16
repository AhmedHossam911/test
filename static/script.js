function searchStudent() {
    const studentId = document.getElementById('studentId').value;
    if (!studentId) {
        alert('Please enter a Student ID');
        return;
    }
    
    fetch(`http://127.0.0.1:8000/search/?student_id=${studentId}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Student not found');
            }
            return response.json();
        })
        .then(data => {
            document.getElementById('result').innerHTML = `
                <p><strong>ID:</strong> ${data.ID}</p>
                <p><strong>Name:</strong> ${data.Name}</p>
                <p><strong>Doctor:</strong> ${data.Doctor}</p>
                <p><strong>Mobile:</strong> ${data.Mobile}</p>
            `;
        })
        .catch(error => {
            document.getElementById('result').innerHTML = `<p style='color: red;'>${error.message}</p>`;
        });
}
