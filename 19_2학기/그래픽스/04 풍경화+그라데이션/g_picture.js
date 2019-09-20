
var gl;

window.onload = function init() {
    var canvas = document.getElementById("gl-canvas");

    gl = WebGLUtils.setupWebGL(canvas);
    if (!gl) { alert("WebGL isn't available"); }

    // vertex position
    var vertices = [
        //background
        vec2(-1, -1),
        vec2(-1, 1),
        vec2(1, 1),
        vec2(1, -1),
        //mt1
        vec2(-0.3, -0.5),
        vec2(0.5, 0.1),
        vec2(1, -0.2),
        vec2(1, -0.8),
        //mt2
        vec2(-1, -0.5),
        vec2(-0.4, -0.1),
        vec2(1, -0.6),
        vec2(1, -1),
        vec2(-1, -1),
        //mt2_shadow
        vec2(1, -0.6),
        vec2(-0.4, -0.1),
        vec2(-0.6, -0.5),
        vec2(-0.4, -0.9),
        vec2(-0.6, -1),
        vec2(1, -1),
    ];

    // vertex color (R, G, B, A)
    var colors = [
        //background
        vec4(105 / 255, 65 / 255, 145 / 255, 1),
        vec4(3 / 255, 9 / 255, 43 / 255, 1),
        vec4(3 / 255, 9 / 255, 43 / 255, 1),
        vec4(105 / 255, 65 / 255, 145 / 255, 1),
        //mt1
        vec4(169 / 255, 71 / 255, 119 / 255, 1),
        vec4(169 / 255, 71 / 255, 119 / 255, 1),
        vec4(169 / 255, 71 / 255, 119 / 255, 1),
        vec4(169 / 255, 71 / 255, 119 / 255, 1),
        //mt2
        vec4(176 / 255, 72 / 255, 125 / 255, 1),
        vec4(191 / 255, 97 / 255, 144 / 255, 1),
        vec4(176 / 255, 72 / 255, 125 / 255, 1),
        vec4(155 / 255, 63 / 255, 109 / 255, 1),
        vec4(155 / 255, 63 / 255, 109 / 255, 1),
        //mt2_shadow
        vec4(121 / 255, 44 / 255, 100 / 255, 1),
        vec4(85 / 255, 35 / 255, 88 / 255, 1),
        vec4(176 / 255, 72 / 255, 125 / 255, 1),
        vec4(155 / 255, 63 / 255, 109 / 255, 1),
        vec4(155 / 255, 63 / 255, 109 / 255, 1),
        vec4(155 / 255, 63 / 255, 109 / 255, 1),
    ];

    //  Configure WebGL
    gl.viewport(0, 0, canvas.width, canvas.height);
    gl.clearColor(0.0, 0.0, 0.0, 1.0);

    //  Load shaders and initialize attribute buffers    
    var program = initShaders(gl, "vertex-shader", "fragment-shader");
    gl.useProgram(program);

    // Create a buffer object, initialize it, and associate it with the
    //  associated attribute variable in our vertex shader    

    /*-----------------------------------------------------------------------*/
    /* vertex position ------------------------------------------------------*/
    /*-----------------------------------------------------------------------*/

    // triangle vertex buffer 
    var vertexPositionBufferId = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, vertexPositionBufferId);
    gl.bufferData(gl.ARRAY_BUFFER, flatten(vertices), gl.STATIC_DRAW);

    var vPosition = gl.getAttribLocation(program, "vPosition");
    gl.vertexAttribPointer(vPosition, 2, gl.FLOAT, false, 0, 0);
    gl.enableVertexAttribArray(vPosition);

    /*-----------------------------------------------------------------------*/
    /* vertex color ---------------------------------------------------------*/
    /*-----------------------------------------------------------------------*/

    var vertexColorBufferId = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, vertexColorBufferId);
    gl.bufferData(gl.ARRAY_BUFFER, flatten(colors), gl.STATIC_DRAW);

    var vColor = gl.getAttribLocation(program, "vColor");
    gl.vertexAttribPointer(vColor, 4, gl.FLOAT, false, 0, 0);
    gl.enableVertexAttribArray(vColor);

    
    // render
    gl.clear(gl.COLOR_BUFFER_BIT);
    gl.drawArrays(gl.TRIANGLE_FAN, 0, 4);
    gl.drawArrays(gl.TRIANGLE_FAN, 4, 4);
    gl.drawArrays(gl.TRIANGLE_FAN, 8, 5);
    gl.drawArrays(gl.TRIANGLE_FAN, 13, 6);

};
