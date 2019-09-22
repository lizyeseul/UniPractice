
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
        //mt1_shadow
        vec2(1, -0.2),
        vec2(0.5, 0.1),
        vec2(0.4,-0.08),
        vec2(0.5, -0.24),
        vec2(0.45, -0.6),
        vec2(1, -0.6),
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
        vec2(-0.4, -1),
        vec2(1, -1),
        //moon
        vec2(-0.5, 0.6),
        vec2(-0.47, 0.7),
        vec2(-0.42, 0.66),
        vec2(-0.4, 0.6),
        vec2(-0.42, 0.54),
        vec2(-0.47, 0.5),
        vec2(-0.53, 0.5),
        vec2(-0.58, 0.54),
        vec2(-0.6, 0.6),
        vec2(-0.58, 0.66),
        vec2(-0.53, 0.7),
        vec2(-0.47, 0.7),
        //star
        vec2(0, 0),
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
        vec4(191 / 255, 97 / 255, 144 / 255, 1),
        vec4(169 / 255, 71 / 255, 119 / 255, 1),
        vec4(169 / 255, 71 / 255, 119 / 255, 1),
        //mt1_shadow
        vec4(169 / 255, 71 / 255, 119 / 255, 1),
        vec4(191 / 255, 97 / 255, 144 / 255, 1),
        vec4(169 / 255, 71 / 255, 119 / 255, 1),
        vec4(135 / 255, 57 / 255, 96 / 255, 1),
        vec4(135 / 255, 57 / 255, 96 / 255, 1),
        vec4(135 / 255, 57 / 255, 96 / 255, 1),
        //mt2
        vec4(176 / 255, 72 / 255, 125 / 255, 1),
        vec4(191 / 255, 97 / 255, 144 / 255, 1),
        vec4(176 / 255, 72 / 255, 125 / 255, 1),
        vec4(155 / 255, 63 / 255, 109 / 255, 1),
        vec4(155 / 255, 63 / 255, 109 / 255, 1),
        //mt2_shadow
        vec4(121 / 255, 44 / 255, 100 / 255, 1),
        vec4(85 / 255, 35 / 255, 88 / 255, 1),
        vec4(166 / 255, 62 / 255, 115 / 255, 1),
        vec4(131 / 255, 54 / 255, 110 / 255, 1),
        vec4(131 / 255, 54 / 255, 110 / 255, 1),
        //moon
        vec4(252 / 255, 237 / 255, 246 / 255, 1),
        vec4(252 / 255, 237 / 255, 246 / 255, 1),
        vec4(252 / 255, 237 / 255, 246 / 255, 1),
        vec4(252 / 255, 237 / 255, 246 / 255, 1),
        vec4(252 / 255, 237 / 255, 246 / 255, 1),
        vec4(252 / 255, 237 / 255, 246 / 255, 1),
        vec4(252 / 255, 237 / 255, 246 / 255, 1),
        vec4(252 / 255, 237 / 255, 246 / 255, 1),
        vec4(252 / 255, 237 / 255, 246 / 255, 1),
        vec4(252 / 255, 237 / 255, 246 / 255, 1),
        vec4(252 / 255, 237 / 255, 246 / 255, 1),
        vec4(252 / 255, 237 / 255, 246 / 255, 1),
        
        //star
        vec4(0 / 255, 0 / 255, 0 / 255, 1),

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


    var vOffset = gl.getUniformLocation(program, "vOffset");
    //star size
    var pointsize = gl.getUniformLocation(program, "a_pointSize");
    //color offset
    var cOffset = gl.getUniformLocation(program, "cOffset");

   

    // render
    gl.uniform4fv(cOffset, [0, 0, 0, 0]);
    gl.clear(gl.COLOR_BUFFER_BIT);
    gl.drawArrays(gl.TRIANGLE_FAN, 0, 4);//background

    //star
    for (var i = 0; i < 100; i++) {
        var r = (Math.random() * 155 + 100) /255;
        var g = (Math.random() * 155 + 100) /255;
        var b = (Math.random() * 155 + 100) /255;
        gl.uniform4fv(cOffset, [r, g, b, 0]);
        var x = Math.random() * 2-1;
        var y = Math.random() * 2 - 1;
        var size = Math.random() * 2+0.1;
        gl.uniform4fv(vOffset, [x, y, 0, 0]);
        gl.uniform1f(pointsize, size);
        gl.drawArrays(gl.POINTS, 36, 1);
    }

    gl.uniform4fv(cOffset, [0, 0, 0, 0]);
    gl.uniform4fv(vOffset, [0, 0, 0, 0]);
    gl.drawArrays(gl.TRIANGLE_FAN, 4, 4);//mt1
    gl.drawArrays(gl.TRIANGLE_FAN, 8, 6);//mt1_shadow
    gl.drawArrays(gl.TRIANGLE_FAN, 14, 5);//mt2
    gl.drawArrays(gl.TRIANGLE_FAN, 19, 5);//mt2+shadow

    //moon
    gl.uniform4fv(vOffset, [0.5, 0, 0, 0]);
    gl.drawArrays(gl.TRIANGLE_FAN, 24, 12);

 

    

};
