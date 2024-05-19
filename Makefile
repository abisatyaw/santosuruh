.PHONY: tw dev

dev:
	@start cmd /c "python src/manage.py runserver && pause"

tw:
	@start cmd /c "pnpm exec tailwind -i ./tailwind.css -o ./src/base/static/css/base.css --watch && pause"
