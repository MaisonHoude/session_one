# === Stage 43: Добавь пагинацию длинных списков ===
# Project: MeetingVault
class Paginator:
    """Compact paginator for long lists with offset-based navigation."""
    
    def __init__(self, data, page_size=10):
        self.data = data
        self.page_size = page_size
        self.total_pages = (len(data) + page_size - 1) // page_size if data else 0
    
    def get_page(self, page, offset=None):
        if offset is None:
            offset = (page - 1) * self.page_size
        return self.data[offset:offset + self.page_size]
    
    def get_page_info(self, page=None):
        if page is None:
            page = 1
        return {
            'page': page,
            'total_pages': self.total_pages,
            'has_next': page < self.total_pages,
            'has_prev': page > 1,
            'current_page': self.get_page(page)
        }
