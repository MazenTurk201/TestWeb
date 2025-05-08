from flet import *

def main(page: Page):
    page.title = "Crud"
    #page.window.maximized = True
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    immg = Container(
        content=Image(
            src=r"image/image.jpg",  # Random image URL
            # src="https://i.gifer.com/WME8.gif",  # Random image URL
            # width=page.width,
            # height=page.height,
            fit=ImageFit.COVER,
        ),)  # Stretch to fit)
    lolg = Image(
            src="https://i.gifer.com/WME8.gif",
            # fit=ImageFit.COVER,
        )
    loginframe = Container(
        content=Column(
            controls=[
                Text("Login Test\n\n", size=30, weight="bold", color="white",),
                TextField(label="Username", width=300,content_padding=Padding(left=20, top=15, right=20, bottom=15)),
                TextField(label="Password", width=300, password=True),
                ElevatedButton("Login", width=300,on_click=lambda e: loginb(e)),
                ElevatedButton("Sign-up", width=300,on_click=lambda e: loginb(e),bgcolor="transparent"),
                # IconButton(
                #     icon=Image(src="https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"),
                #     tooltip="Google",  # Tooltip text
                #     on_click=lambda e: print("Google button clicked"),  # Action on click
                # )
                # Text("Sign-up", size=30,color="white",),
                # lolg,
            ],
            alignment="center",
            horizontal_alignment="center",
            spacing=20,
        ),
        padding=40,
        bgcolor="transparent",  # Semi-transparent white background
        border_radius=25,
        width=400,
        height=600,
        blur=10,
        border=Border(
            left=BorderSide(width=2, color=Colors.WHITE24),
            top=BorderSide(width=2, color=Colors.WHITE24),
            right=BorderSide(width=2, color=Colors.WHITE24),
            bottom=BorderSide(width=2, color=Colors.WHITE24),
        ),
        shadow=BoxShadow(
            spread_radius=1,
            blur_radius=55,
            color=Colors.BLACK54,
            offset=Offset(5, 5),
        ),
    )
    def route_change(route):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    Container(Stack([immg,Container(loginframe,alignment=alignment.center,padding=75)]),),
                ],
            )
        )
        if page.route == "/store":
            page.views.append(
                View(
                    "/store",
                    [
                        # AppBar(title=Text("Store"), bgcolor=Colors.SURFACE_VARIANT),
                        Container(
                        content=Column(
                                controls=[
                                    Text("Hello, Flet!", color="white", size=30,),
                                    ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                                    ElevatedButton("Login", on_click=lambda e: loginb(e),),
                                    ],
                                alignment=MainAxisAlignment.CENTER,
                                horizontal_alignment=CrossAxisAlignment.CENTER
                                ),
                        image_src=r"assets\image.jpg",
                        # image_fit=ImageFit.COVER,  # Stretch to fit
                        width=page.width,
                        height=page.height,
                        expand=True  # Fill the screen
                        ),
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    def loginb(e):
        print("login")
        page.go("/store")




    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    
if __name__ == "__main__":
    # app(main,view=WEB_BROWSER,port=80,assets_dir="assets",)
    app(main,assets_dir="assets")
