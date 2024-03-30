{ pkgs }: {
    deps = [
      pkgs.glibcLocales
      pkgs.geckodriver
      pkgs.ungoogled-chromium
      pkgs.chromedriver
      pkgs.cowsay
    ];
}