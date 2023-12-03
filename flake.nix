{
  description = "Basic Python environment";

  inputs = {
    nixpkgs.url = github:NixOS/nixpkgs/nixos-unstable;

  };

  outputs = { self, nixpkgs, ... }: 
  let
    system = "x86_64-linux";
    pkgs = nixpkgs.legacyPackages.${system};
    pythonPackages = pkgs.python311Packages;
  
    impurePythonEnv = pkgs.mkShell rec {
      name = "impurePythonEnv";
      venvDir = "./.venv";
      buildInputs = [
        pythonPackages.python
        pythonPackages.venvShellHook
        pkgs.autoPatchelfHook

        pythonPackages.python-dotenv
        pythonPackages.psutil
        pythonPackages.pandas
        pythonPackages.numpy
        pythonPackages.seaborn
        pythonPackages.matplotlib
        pythonPackages.pandas-stubs
        pythonPackages.types-psutil
      ];

      postVenvCreation = ''
        unset SOURCE_DATE_EPOCH
        pip install -r requirements.txt
        autoPatchelf ./venv
      '';

      postShellHook = ''
        unset SOURCE_DATE_EPOCH
      '';
    };

  in {
      # Expose the environment as a default package
      defaultPackage.x86_64-linux = impurePythonEnv;
    };
}
