document.getElementById('downloadBtn').addEventListener('click', function() {
    // Update the path to reflect the structure within the 'static' folder
    const downloadLink = './static/motiondetector2.exe';

    // Create a link element
    const link = document.createElement('a');
    link.href = downloadLink;
    link.download = 'motiondetector2.exe'; // The default name for the downloaded file

    // Append the link to the document and trigger a click event
    document.body.appendChild(link);
    link.click();

    // Remove the link from the document
    document.body.removeChild(link);
});
