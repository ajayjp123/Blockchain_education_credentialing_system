document.getElementById('storeForm').addEventListener('submit', async function (event) {
    event.preventDefault();
    const formData = new FormData(this);
    const response = await fetch('/store_credential/', {
        method: 'POST',
        body: formData
    });
    const data = await response.json();
    console.log(data);
});

document.getElementById('verifyForm').addEventListener('submit', async function (event) {
    event.preventDefault();
    const student_id = document.getElementById('verify_student_id').value;
    const response = await fetch(`/verify_credential/?student_id=${student_id}`);
    const data = await response.json();
    document.getElementById('result').innerHTML = JSON.stringify(data);
});
