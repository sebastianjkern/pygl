varying vec2 uv;

void main() {
    gl_FragColor = vec4(1-uv.y, 1-uv.x, 1.0,  1.0);
}