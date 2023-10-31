// Copyright Epic Games, Inc. All Rights Reserved.

using System.Collections.Generic;
using System.IO;
using UnrealBuildTool;

public class MongoDBSDK : ModuleRules
{
	private List<string> LibraryNames = new List<string>()
	{
		"bson-1.0",
		"bsoncxx",
		"mongoc-1.0",
		"mongocxx"
	};
	
	public MongoDBSDK(ReadOnlyTargetRules Target) : base(Target)
	{
		Type = ModuleType.External;
		PCHUsage = ModuleRules.PCHUsageMode.UseExplicitOrSharedPCHs;
		
		PublicIncludePaths.AddRange(
			new string[] {
				// ... add public include paths required here ...
				Path.Combine(ModuleDirectory, "Include")
			}
		);
				
		
		PrivateIncludePaths.AddRange(
			new string[] {
				// ... add other private include paths required here ...
			}
		);
			
		
		PublicDependencyModuleNames.AddRange(
			new string[]
			{
				"Core",
				// ... add other public dependencies that you statically link with here ...
			}
		);
			
		
		PrivateDependencyModuleNames.AddRange(
			new string[]
			{
				"CoreUObject",
				"Engine",
				"Slate",
				"SlateCore",
				// ... add private dependencies that you statically link with here ...	
			}
		);
		
		
		DynamicallyLoadedModuleNames.AddRange(
			new string[]
			{
				// ... add any modules that your module loads dynamically here ...
			}
		);

		foreach (string lib in LibraryNames)
		{
			string LibraryPath = Path.Combine(ModuleDirectory, "Binaries");
			PublicAdditionalLibraries.Add(Path.Combine(LibraryPath, lib + ".lib"));
			RuntimeDependencies.Add("$(BinaryOutputDir)/" + lib + ".dll", Path.Combine(LibraryPath, lib + ".dll"));
		}
	}
}