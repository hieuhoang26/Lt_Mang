from urllib.request import Request, urlopen
import gzip

def main():
    url = 'http://www.python.org'  # URL mục tiêu

    try:
        # Tạo một request
        request = Request(url)
        request.add_header('Accept-Language', 'vi')  # Thêm header cho request

        # Gửi request và nhận phản hồi
        response = urlopen(request)

        # Hiển thị thông tin từ request và response
        print("User-Agent:", request.get_header('User-agent'))

        print("\nDòng đầu tiên của HTML:")
        print(response.readline().decode('utf-8'))  # Đọc một dòng đầu tiên

        print("\nToàn bộ HTML của trang web:")
        content = response.read()

        # Kiểm tra nếu nội dung được mã hóa gzip, giải nén nếu cần
        if response.getheader('Content-Encoding') == 'gzip':
            content = gzip.decompress(content)

        print(content.decode('utf-8'))  # Hiển thị nội dung

        # Hiển thị URL phản hồi cuối cùng
        print("\nURL của trang phản hồi:", response.url)

        # Hiển thị mã trạng thái HTTP
        print("\nStatus code:", response.status)

        # Hiển thị tất cả các headers
        print("\nHeaders của trang web:")
        for header in response.getheaders():
            print(header)

        # Lấy và kiểm tra giá trị header 'Content-Type'
        content_type = response.getheader('Content-Type')
        print("\nContent-Type:", content_type)

        # Phân tách MIME type và tham số nếu tồn tại
        if content_type and ';' in content_type:
            mime_type, params = content_type.split(';', 1)
            print("MIME Type:", mime_type.strip())
            print("Params:", params.strip())

    except Exception as e:
        print("Đã xảy ra lỗi:", e)

if __name__ == "__main__":
    main()