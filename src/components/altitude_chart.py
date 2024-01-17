import flet as ft


def get_plot_altitude_chart(data_points):
    chart_data = [
        ft.LineChartData(
            data_points=data_points,
            color=ft.colors.CYAN,
            stroke_width=5,
            curved=True,
            stroke_cap_round=True,
        )
    ]

    chart = ft.LineChart(
        data_series=chart_data,
        border=ft.border.all(3, ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE)),
        horizontal_grid_lines=ft.ChartGridLines(
            interval=1, color=ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE), width=1
        ),
        vertical_grid_lines=ft.ChartGridLines(
            interval=1, color=ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE), width=1
        ),
        left_axis=ft.ChartAxis(
            title=ft.Text("Altitude (m)"),
            labels_size=40,
        ),
        bottom_axis=ft.ChartAxis(
            title=ft.Text("Time (s)"),
            labels_size=32,
        ),
        tooltip_bgcolor=ft.colors.with_opacity(0.8, ft.colors.BLUE_GREY),
        min_y=0,
        max_y=max(point.y for point in data_points),
        min_x=min(point.x for point in data_points),
        max_x=max(point.x for point in data_points),
        width=500,
        height=400,
    )

    return chart
