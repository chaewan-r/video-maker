#!/usr/bin/env python3
"""
FFmpeg.wasm을 위한 로컬 서버
SharedArrayBuffer를 사용하기 위해 필요한 CORS 헤더를 설정합니다.
"""

from http.server import HTTPServer, SimpleHTTPRequestHandler
import sys

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # FFmpeg.wasm이 SharedArrayBuffer를 사용하기 위한 필수 헤더
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        self.send_header('Cross-Origin-Resource-Policy', 'cross-origin')
        super().end_headers()

def run(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, CORSRequestHandler)
    print(f'🚀 서버 시작: http://localhost:{port}')
    print(f'📁 실행 디렉토리: {httpd.server_name}')
    print(f'✅ FFmpeg.wasm 지원 활성화 (SharedArrayBuffer)')
    print(f'\n🌐 브라우저에서 열기: http://localhost:{port}/standalone.html')
    print(f'\n⏹️  서버 중지: Ctrl+C\n')
    httpd.serve_forever()

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    run(port)
