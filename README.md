# Xây dựng trang đấu giá trực tuyến
Đây là đồ án tốt nghiệp xây dựng trang đấu giá trực tuyến sử dụng công nghệ **Django**, ngôn ngữ **Python** và hệ quản trị cơ sở dữ liệu **MySQL** để lưu trữ dữ liệu

![image](https://github.com/niveqhost/finalYearProject/blob/dev/auction.jpg)
![image](https://github.com/niveqhost/finalYearProject/blob/dev/auction-2.jpg)
![image](https://github.com/niveqhost/finalYearProject/blob/dev/auction-3.jpg)

Khi chạy ứng dụng cần tùy biến file .env theo cách của bạn

#### Cài đặt các công cụ cần thiết để chạy ứng dụng

Mở cửa sổ Command Prompt, di chuyển đến thư mục gốc chứa chương trình và chạy lệnh:
```bash
pip install -r requirements.txt
```

#### Các tính năng chính của chương trình
Hỗ trợ đa ngôn ngữ (Tiếng Anh - Tiếng Việt)

<h2>Mô tả cụ thể: </h2>
 
<h4>Tạo phiên đấu giá: </h4>
<li>
 Users will be able to visit a page to create a new listing. They will be able to specify a title for the listing, a text-based description, and what the starting bid should be. Users can also optionally add an URL for an image for the listing and/or a category (e.g. Fashion, Toys, Electronics, Home, etc.).
</li>

<h4>Các phiên đấu giá đang diễn ra: </h4>
<li>
 The default route let users view all of the currently active auction listings. For each active listing, this page display the title, description, current price, and photo (if one exists for the listing).
</li>

<h4>Chi tiết phiên đấu giá: </h4>
<li>
 Clicking on a listing take users to a page specific to that listing. On that page, users will be able to view all details about the listing, including the current price for the listing.
  <li>If the user is signed in, the user will be able to add the item to their “Watchlist.” If the item is already on the watchlist, the user will be able to remove it.</li>
  <li>If the user is signed in, the user will be able to bid on the item. The bid must be at least as large as the starting bid, and must be greater than any other bids that have been placed (if any). If the bid doesn’t meet those criteria, the user will be presented with an error.</li>
  <li>If the user is signed in and is the one who created the listing, the user have the ability to “close” the auction from this page, which makes the highest bidder the winner of the auction and makes the listing no longer active.</li>
  <li>Users who are signed in will be able to add comments to the listing page. The listing page displays all comments that have been made on the listing.</li>
</li>

<h4>Danh sách ưa thích: </h4>
<li>
 Users who are signed in will be able to visit a Watchlist page, which displays all of the listings that a user has added to their watchlist. Clicking on any of those listings take the user to that listing’s page.
</li>

<h4>Danh mục sản phẩm: </h4>
<li>
 Users will be able to visit a page that displays a list of all listing categories. Clicking on the name of any category takes the user to a page that displays all of the active listings in that category.
</li>

<h4>Giao diện trang quản trị: </h4>
<li>
Via the Django admin interface, a site administrator will be able to view, add, edit, and delete any listings, comments, and bids made on the site.
</li>
