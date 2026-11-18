import os
import json
import logging

from sqlalchemy import create_engine, text

# Cấu hình logging
logging.basicConfig(level=logging.INFO)

# Đường dẫn lưu dữ liệu
DATA_DIR = "/app/data"

# Đọc thông tin kết nối MySQL
# DB_URL = os.getenv("DB_URL")
DB_URL="mysql+pymysql://root:123456@mysql:3306/ecommerce_db?charset=utf8mb4"

if not DB_URL:
    raise ValueError("DB_URL environment variable is not set")

# Khởi tạo SQLAlchemy Engine
engine = create_engine(DB_URL)

# Tạo logger
_logger = logging.getLogger(__name__)


def extract_products_data(output_file: str):

    _logger.info("Starting data extraction from the database.")
    try:
    # Kết nối database
        with engine.connect() as connection:

            # Câu lệnh SQL
            query = text("""
                SELECT *
                FROM products
                WHERE status = 'active'
            """)

            # Thực thi SQL
            result = connection.execute(query)

            # Mở file để ghi dữ liệu
            with open(output_file, "w", encoding="utf-8") as f:

                # Duyệt từng sản phẩm
                for row in result:

                    # Xử lý dữ liệu NULL
                    safe_desc = row.description if row.description else "Không có mô tả"
                    safe_category = row.category if row.category else "Không có danh mục"
                    safe_price = row.price if row.price is not None else 0.0

                    # Chuyển thông tin sản phẩm thành văn bản
                    context_text = (
                        f"Product Name: {row.name}\n"
                        f"Description: {safe_desc}\n"
                        f"Category: {safe_category}\n"
                        f"Price: {safe_price}"
                    )

                    # Tạo document
                    doc = {
                        "doc_id": f"prod_{row.product_id}",
                        "content": context_text,
                        "metadata": {
                            "description": safe_desc,
                            "category": safe_category,
                            "price": float(safe_price)
                        }
                    }

                    # Ghi document vào file
                    f.write(json.dumps(doc, ensure_ascii=False) + "\n")

        _logger.info(f"Data extraction completed to {output_file}.")
    except Exception as e:
        raise Exception(f"Error occurred during data extraction: {str(e)}")

if __name__ == "__main__":
    output_file = "/app/data/products_data.jsonl"
    _logger.info("Starting data extraction from the database.")
    try:
        extract_products_data(output_file)

        print(" Kieem tra file data/products_data.jsonl xem có dữ liệu không nhé!")
        if os.path.exists(output_file):
            with open(output_file, "r", encoding="utf-8") as f:
                for i, line in enumerate(f):
                    if i <= 10:  # Chỉ in ra 10 dòng đầu tiên
                        #format sang Json
                        parsed_json = json.loads(line)
                        print(json.dumps(parsed_json, ensure_ascii=False, indent=4))
                    else:
                        print("Khong có dữ liệu trong file.")
    except Exception as e:
        _logger.error(f"Error occurred: {str(e)}")