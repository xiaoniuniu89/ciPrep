let htmlEditor = CodeMirror(document.querySelector('.editor .code .html-code'), {
    lineNumbers:true,
    tabSize: 4,
    mode: "xml",
    value: `<h1 class='welcome'>Welcome to the show</h1>`
});

const cssEditor = CodeMirror(document.querySelector('.editor .code .css-code'), {
    lineNumbers:true,
    tabSize: 4,
    mode: "css",
    value: `.welcome {
    color: red;
}`
});

const jsEditor = CodeMirror(document.querySelector('.editor .code .javascript-code'), {
    lineNumbers:true,
    tabSize: 4,
    lineWrapping: true,
    mode: "javascript",
});

console.log(htmlEditor)




document.querySelector('#run-btn').addEventListener('click', function(){
    console.log('ran')
    let htmlCode = htmlEditor.getValue()
    let cssCode = '<style>' + cssEditor.getValue() + '</style>'
    let jsCode = '<scri' + 'pt>' + jsEditor.getValue() + '</scri' + 'pt>'
    let previewWindow = document.querySelector('#preview-window').contentWindow.document
    previewWindow.open()
    previewWindow.write(htmlCode+cssCode+jsCode)
    previewWindow.close()
})

const roomName = JSON.parse(document.getElementById('room-name').textContent);
const chatSocket = new WebSocket(
    'ws://' +
    window.location.host +
    '/ws/editor/' +
    roomName +
    '/'
)

const htmlEventDiv = document.querySelector('.html-code')
const cssEventDiv = document.querySelector('.css-code')
const jsEventDiv = document.querySelector('.javascript-code')

const sendData = (value, eventDiv, line, ch) => {
    chatSocket.send(JSON.stringify({
        'value': value,
        'eventDiv': eventDiv,
        'line': line,
        'ch': ch
    }));
}

htmlEventDiv.addEventListener('keyup', (e) => {
    console.log(htmlEditor.getValue())
    const {line, ch} = htmlEditor.getCursor()
    console.log(line, ch)
     sendData(htmlEditor.getValue(), '.html-code', line, ch)
     })
// htmlEventDiv.addEventListener('keyup', (e) => { sendData(e, htmlEventDiv) })
// htmlEventDiv.addEventListener('keyup', (e) => { sendData(e, htmlEventDiv) })

chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    // console.log(data)
    if(data.eventDiv === ".html-code") {
        htmlEditor.setValue(data.value)
        htmlEditor.setCursor(data.line, data.ch)
    }
    
}
