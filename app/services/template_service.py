from jinja2 import Environment, FileSystemLoader

class TemplateService:
    def __init__(self):
        self.env = Environment(loader=FileSystemLoader('app/templates'))

    def render_receipt(self, context: dict) -> str:
        template = self.env.get_template('receipt.html')
        return template.render(context)
