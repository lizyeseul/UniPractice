
var gl;

window.onload = function init()
{
    var canvas = document.getElementById( "gl-canvas" );
    
    gl = WebGLUtils.setupWebGL( canvas );
    if ( !gl ) { alert( "WebGL isn't available" ); }

    //  Configure WebGL
    var r = 157 / 256;
    var g = 195 / 256;
    var b = 230 / 256;
    gl.viewport( 0, 0, canvas.width, canvas.height);
    gl.clearColor(r,g,b, 1.0);

    //  Load shaders and initialize 
    var program = initShaders( gl, "vertex-shader", "fragment-shader" );

	gl.useProgram( program );   

    // create a buffer on gpu and bind point    
    var bufferId = gl.createBuffer();
    gl.bindBuffer( gl.ARRAY_BUFFER, bufferId ); 

    // Associate out shader variables with our data buffer   	
	// attribute variable
    var vPosition = gl.getAttribLocation( program, "vPosition" );
    gl.vertexAttribPointer( vPosition, 2, gl.FLOAT, false, 0, 0);
    gl.enableVertexAttribArray( vPosition );

	// uniform variable
    var fColor = gl.getUniformLocation(program, "fColor");
    var vOffset = gl.getUniformLocation(program, "vOffset");

	// clear buffer bit
	gl.clear(gl.COLOR_BUFFER_BIT);


    //ÆÄ¶õ ¹Ù´Ú
	var blue = new Float32Array([
        -1, -1,
        -1, -0.5,
        1, -0.5,
        1, -1
	]);
	gl.bufferData(gl.ARRAY_BUFFER, blue, gl.STATIC_DRAW);
	gl.uniform4fv(fColor, [0, 112 / 255, 192 / 255, 1]);
	gl.drawArrays(gl.TRIANGLE_FAN, 0, 4);

    //Áý ¸öÃ¼
	var house = new Float32Array([
        -0.6, -0.3,
        -0.6, 0,
        0.02, 0,
        0.02, -0.3
	]);
	gl.bufferData(gl.ARRAY_BUFFER, house, gl.STATIC_DRAW);
	gl.uniform4fv(fColor, [175/255, 171 / 255, 171 / 255, 1]);
	gl.drawArrays(gl.TRIANGLE_FAN, 0, 4);

    //ÁöºØ
	var roof = new Float32Array([
        -0.8, 0,
        -0.55, 0.32,
        -0.55, 0,
        -0.05, 0.32,
        -0.05, 0,
        0.2, 0
	]);
	gl.bufferData(gl.ARRAY_BUFFER, roof, gl.STATIC_DRAW);
	gl.uniform4fv(fColor, [255 / 255, 230 / 255, 153 / 255, 1]);
	gl.drawArrays(gl.TRIANGLE_STRIP, 0, 6);

    //Ã¢¹®
	var window = new Float32Array([
        -0.29, -0.19,
        -0.29, -0.02,
        -0.18, -0.02,
        -0.18, -0.19
	]);
	gl.bufferData(gl.ARRAY_BUFFER, window, gl.STATIC_DRAW);
	gl.uniform4fv(fColor, [231 / 255, 230 / 255, 230 / 255, 1]);
	gl.drawArrays(gl.TRIANGLE_FAN, 0, 4);

	gl.uniform4fv(vOffset, [0.13, 0, 0, 0]);
	gl.drawArrays(gl.TRIANGLE_FAN, 0, 4);

    //³ª¹«
	var tree = new Float32Array([
        -0.2, 0,
        0, 0.25,
        0.2, 0,
        -0.2, -0.25,
        0, 0,
        0.2, -0.25,

        -0.08, -0.53,
        -0.08, -0.25,
        0.08, -0.25,
        0.08, -0.53
	]);

	gl.bufferData(gl.ARRAY_BUFFER, tree, gl.STATIC_DRAW);

	gl.uniform4fv(vOffset, [0, 0, 0, 0]);
	draw_tree(fColor);

	for (var i = 0; i < 20; i++) {
	    tree[i] *= 1.2;
	}
	gl.bufferData(gl.ARRAY_BUFFER, tree, gl.STATIC_DRAW);
	gl.uniform4fv(vOffset, [0.55, 0.1, 0, 0]);
	draw_tree(fColor);

	for(var i=0; i<20; i++){
	    tree[i] *= 0.7;
	}
	gl.bufferData(gl.ARRAY_BUFFER, tree, gl.STATIC_DRAW);
	gl.uniform4fv(vOffset, [-0.8, -0.1, 0, 0]);
	draw_tree(fColor);


    //±¼¶Ò
	var chim = new Float32Array([
        -0.4, 0.22,
        -0.55, 0.1,
        -0.55, 0.4,
        -0.4, 0.4
	]);
	gl.bufferData(gl.ARRAY_BUFFER, chim, gl.STATIC_DRAW);
	gl.uniform4fv(fColor, [255 / 255, 175 / 255, 175 / 255, 1]);
	gl.uniform4fv(vOffset, [0, 0, 0, 0]);
	gl.drawArrays(gl.TRIANGLE_FAN, 0, 4);
	
};
function draw_tree(fColor) {
    gl.uniform4fv(fColor, [0, 176 / 255, 80 / 255, 1]);
    gl.drawArrays(gl.TRIANGLES, 0, 6);
    gl.uniform4fv(fColor, [127 / 255, 96 / 255, 0, 1]);
    gl.drawArrays(gl.TRIANGLE_FAN, 6, 4);
}
