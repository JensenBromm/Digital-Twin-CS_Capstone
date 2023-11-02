// Copyright Epic Games, Inc. All Rights Reserved.
/*===========================================================================
	Generated code exported from UnrealHeaderTool.
	DO NOT modify this manually! Edit the corresponding .h files instead!
===========================================================================*/

#include "UObject/GeneratedCppIncludes.h"
#include "RobotProj/RobotMover.h"
PRAGMA_DISABLE_DEPRECATION_WARNINGS
void EmptyLinkFunctionForGeneratedCodeRobotMover() {}
// Cross Module References
	COREUOBJECT_API UClass* Z_Construct_UClass_UClass();
	COREUOBJECT_API UScriptStruct* Z_Construct_UScriptStruct_FVector();
	ENGINE_API UClass* Z_Construct_UClass_AActor();
	ROBOTPROJ_API UClass* Z_Construct_UClass_ADatabaseConnection_NoRegister();
	ROBOTPROJ_API UClass* Z_Construct_UClass_ARobotMover();
	ROBOTPROJ_API UClass* Z_Construct_UClass_ARobotMover_NoRegister();
	UPackage* Z_Construct_UPackage__Script_RobotProj();
// End Cross Module References
	void ARobotMover::StaticRegisterNativesARobotMover()
	{
	}
	IMPLEMENT_CLASS_NO_AUTO_REGISTRATION(ARobotMover);
	UClass* Z_Construct_UClass_ARobotMover_NoRegister()
	{
		return ARobotMover::StaticClass();
	}
	struct Z_Construct_UClass_ARobotMover_Statics
	{
		static UObject* (*const DependentSingletons[])();
#if WITH_METADATA
		static const UECodeGen_Private::FMetaDataPairParam Class_MetaDataParams[];
#endif
#if WITH_METADATA
		static const UECodeGen_Private::FMetaDataPairParam NewProp_robotVelocity_MetaData[];
#endif
		static const UECodeGen_Private::FStructPropertyParams NewProp_robotVelocity;
#if WITH_METADATA
		static const UECodeGen_Private::FMetaDataPairParam NewProp_startLocation_MetaData[];
#endif
		static const UECodeGen_Private::FStructPropertyParams NewProp_startLocation;
#if WITH_METADATA
		static const UECodeGen_Private::FMetaDataPairParam NewProp_distance_MetaData[];
#endif
		static const UECodeGen_Private::FDoublePropertyParams NewProp_distance;
#if WITH_METADATA
		static const UECodeGen_Private::FMetaDataPairParam NewProp_moveDistance_MetaData[];
#endif
		static const UECodeGen_Private::FDoublePropertyParams NewProp_moveDistance;
#if WITH_METADATA
		static const UECodeGen_Private::FMetaDataPairParam NewProp_x_MetaData[];
#endif
		static const UECodeGen_Private::FDoublePropertyParams NewProp_x;
#if WITH_METADATA
		static const UECodeGen_Private::FMetaDataPairParam NewProp_z_MetaData[];
#endif
		static const UECodeGen_Private::FDoublePropertyParams NewProp_z;
#if WITH_METADATA
		static const UECodeGen_Private::FMetaDataPairParam NewProp_DatabaseClass_MetaData[];
#endif
		static const UECodeGen_Private::FClassPropertyParams NewProp_DatabaseClass;
		static const UECodeGen_Private::FPropertyParamsBase* const PropPointers[];
		static const FCppClassTypeInfoStatic StaticCppClassTypeInfo;
		static const UECodeGen_Private::FClassParams ClassParams;
	};
	UObject* (*const Z_Construct_UClass_ARobotMover_Statics::DependentSingletons[])() = {
		(UObject* (*)())Z_Construct_UClass_AActor,
		(UObject* (*)())Z_Construct_UPackage__Script_RobotProj,
	};
	static_assert(UE_ARRAY_COUNT(Z_Construct_UClass_ARobotMover_Statics::DependentSingletons) < 16);
#if WITH_METADATA
	const UECodeGen_Private::FMetaDataPairParam Z_Construct_UClass_ARobotMover_Statics::Class_MetaDataParams[] = {
		{ "IncludePath", "RobotMover.h" },
		{ "ModuleRelativePath", "RobotMover.h" },
	};
#endif
#if WITH_METADATA
	const UECodeGen_Private::FMetaDataPairParam Z_Construct_UClass_ARobotMover_Statics::NewProp_robotVelocity_MetaData[] = {
		{ "Category", "Robot_Mover" },
		{ "ModuleRelativePath", "RobotMover.h" },
	};
#endif
	const UECodeGen_Private::FStructPropertyParams Z_Construct_UClass_ARobotMover_Statics::NewProp_robotVelocity = { "robotVelocity", nullptr, (EPropertyFlags)0x0040000000000001, UECodeGen_Private::EPropertyGenFlags::Struct, RF_Public|RF_Transient|RF_MarkAsNative, nullptr, nullptr, 1, STRUCT_OFFSET(ARobotMover, robotVelocity), Z_Construct_UScriptStruct_FVector, METADATA_PARAMS(UE_ARRAY_COUNT(Z_Construct_UClass_ARobotMover_Statics::NewProp_robotVelocity_MetaData), Z_Construct_UClass_ARobotMover_Statics::NewProp_robotVelocity_MetaData) };
#if WITH_METADATA
	const UECodeGen_Private::FMetaDataPairParam Z_Construct_UClass_ARobotMover_Statics::NewProp_startLocation_MetaData[] = {
		{ "Category", "RobotMover" },
		{ "ModuleRelativePath", "RobotMover.h" },
	};
#endif
	const UECodeGen_Private::FStructPropertyParams Z_Construct_UClass_ARobotMover_Statics::NewProp_startLocation = { "startLocation", nullptr, (EPropertyFlags)0x0040000000000001, UECodeGen_Private::EPropertyGenFlags::Struct, RF_Public|RF_Transient|RF_MarkAsNative, nullptr, nullptr, 1, STRUCT_OFFSET(ARobotMover, startLocation), Z_Construct_UScriptStruct_FVector, METADATA_PARAMS(UE_ARRAY_COUNT(Z_Construct_UClass_ARobotMover_Statics::NewProp_startLocation_MetaData), Z_Construct_UClass_ARobotMover_Statics::NewProp_startLocation_MetaData) };
#if WITH_METADATA
	const UECodeGen_Private::FMetaDataPairParam Z_Construct_UClass_ARobotMover_Statics::NewProp_distance_MetaData[] = {
		{ "Category", "RobotMover" },
		{ "ModuleRelativePath", "RobotMover.h" },
	};
#endif
	const UECodeGen_Private::FDoublePropertyParams Z_Construct_UClass_ARobotMover_Statics::NewProp_distance = { "distance", nullptr, (EPropertyFlags)0x0040000000020001, UECodeGen_Private::EPropertyGenFlags::Double, RF_Public|RF_Transient|RF_MarkAsNative, nullptr, nullptr, 1, STRUCT_OFFSET(ARobotMover, distance), METADATA_PARAMS(UE_ARRAY_COUNT(Z_Construct_UClass_ARobotMover_Statics::NewProp_distance_MetaData), Z_Construct_UClass_ARobotMover_Statics::NewProp_distance_MetaData) };
#if WITH_METADATA
	const UECodeGen_Private::FMetaDataPairParam Z_Construct_UClass_ARobotMover_Statics::NewProp_moveDistance_MetaData[] = {
		{ "Category", "RobotMover" },
		{ "ModuleRelativePath", "RobotMover.h" },
	};
#endif
	const UECodeGen_Private::FDoublePropertyParams Z_Construct_UClass_ARobotMover_Statics::NewProp_moveDistance = { "moveDistance", nullptr, (EPropertyFlags)0x0040000000000001, UECodeGen_Private::EPropertyGenFlags::Double, RF_Public|RF_Transient|RF_MarkAsNative, nullptr, nullptr, 1, STRUCT_OFFSET(ARobotMover, moveDistance), METADATA_PARAMS(UE_ARRAY_COUNT(Z_Construct_UClass_ARobotMover_Statics::NewProp_moveDistance_MetaData), Z_Construct_UClass_ARobotMover_Statics::NewProp_moveDistance_MetaData) };
#if WITH_METADATA
	const UECodeGen_Private::FMetaDataPairParam Z_Construct_UClass_ARobotMover_Statics::NewProp_x_MetaData[] = {
		{ "Category", "RobotMover" },
		{ "ModuleRelativePath", "RobotMover.h" },
	};
#endif
	const UECodeGen_Private::FDoublePropertyParams Z_Construct_UClass_ARobotMover_Statics::NewProp_x = { "x", nullptr, (EPropertyFlags)0x0040000000020001, UECodeGen_Private::EPropertyGenFlags::Double, RF_Public|RF_Transient|RF_MarkAsNative, nullptr, nullptr, 1, STRUCT_OFFSET(ARobotMover, x), METADATA_PARAMS(UE_ARRAY_COUNT(Z_Construct_UClass_ARobotMover_Statics::NewProp_x_MetaData), Z_Construct_UClass_ARobotMover_Statics::NewProp_x_MetaData) };
#if WITH_METADATA
	const UECodeGen_Private::FMetaDataPairParam Z_Construct_UClass_ARobotMover_Statics::NewProp_z_MetaData[] = {
		{ "Category", "RobotMover" },
		{ "ModuleRelativePath", "RobotMover.h" },
	};
#endif
	const UECodeGen_Private::FDoublePropertyParams Z_Construct_UClass_ARobotMover_Statics::NewProp_z = { "z", nullptr, (EPropertyFlags)0x0040000000020001, UECodeGen_Private::EPropertyGenFlags::Double, RF_Public|RF_Transient|RF_MarkAsNative, nullptr, nullptr, 1, STRUCT_OFFSET(ARobotMover, z), METADATA_PARAMS(UE_ARRAY_COUNT(Z_Construct_UClass_ARobotMover_Statics::NewProp_z_MetaData), Z_Construct_UClass_ARobotMover_Statics::NewProp_z_MetaData) };
#if WITH_METADATA
	const UECodeGen_Private::FMetaDataPairParam Z_Construct_UClass_ARobotMover_Statics::NewProp_DatabaseClass_MetaData[] = {
		{ "Category", "DatabaseConnection" },
		{ "ModuleRelativePath", "RobotMover.h" },
	};
#endif
	const UECodeGen_Private::FClassPropertyParams Z_Construct_UClass_ARobotMover_Statics::NewProp_DatabaseClass = { "DatabaseClass", nullptr, (EPropertyFlags)0x0044000000000001, UECodeGen_Private::EPropertyGenFlags::Class, RF_Public|RF_Transient|RF_MarkAsNative, nullptr, nullptr, 1, STRUCT_OFFSET(ARobotMover, DatabaseClass), Z_Construct_UClass_UClass, Z_Construct_UClass_ADatabaseConnection_NoRegister, METADATA_PARAMS(UE_ARRAY_COUNT(Z_Construct_UClass_ARobotMover_Statics::NewProp_DatabaseClass_MetaData), Z_Construct_UClass_ARobotMover_Statics::NewProp_DatabaseClass_MetaData) };
	const UECodeGen_Private::FPropertyParamsBase* const Z_Construct_UClass_ARobotMover_Statics::PropPointers[] = {
		(const UECodeGen_Private::FPropertyParamsBase*)&Z_Construct_UClass_ARobotMover_Statics::NewProp_robotVelocity,
		(const UECodeGen_Private::FPropertyParamsBase*)&Z_Construct_UClass_ARobotMover_Statics::NewProp_startLocation,
		(const UECodeGen_Private::FPropertyParamsBase*)&Z_Construct_UClass_ARobotMover_Statics::NewProp_distance,
		(const UECodeGen_Private::FPropertyParamsBase*)&Z_Construct_UClass_ARobotMover_Statics::NewProp_moveDistance,
		(const UECodeGen_Private::FPropertyParamsBase*)&Z_Construct_UClass_ARobotMover_Statics::NewProp_x,
		(const UECodeGen_Private::FPropertyParamsBase*)&Z_Construct_UClass_ARobotMover_Statics::NewProp_z,
		(const UECodeGen_Private::FPropertyParamsBase*)&Z_Construct_UClass_ARobotMover_Statics::NewProp_DatabaseClass,
	};
	const FCppClassTypeInfoStatic Z_Construct_UClass_ARobotMover_Statics::StaticCppClassTypeInfo = {
		TCppClassTypeTraits<ARobotMover>::IsAbstract,
	};
	const UECodeGen_Private::FClassParams Z_Construct_UClass_ARobotMover_Statics::ClassParams = {
		&ARobotMover::StaticClass,
		"Engine",
		&StaticCppClassTypeInfo,
		DependentSingletons,
		nullptr,
		Z_Construct_UClass_ARobotMover_Statics::PropPointers,
		nullptr,
		UE_ARRAY_COUNT(DependentSingletons),
		0,
		UE_ARRAY_COUNT(Z_Construct_UClass_ARobotMover_Statics::PropPointers),
		0,
		0x009000A4u,
		METADATA_PARAMS(UE_ARRAY_COUNT(Z_Construct_UClass_ARobotMover_Statics::Class_MetaDataParams), Z_Construct_UClass_ARobotMover_Statics::Class_MetaDataParams)
	};
	static_assert(UE_ARRAY_COUNT(Z_Construct_UClass_ARobotMover_Statics::PropPointers) < 2048);
	UClass* Z_Construct_UClass_ARobotMover()
	{
		if (!Z_Registration_Info_UClass_ARobotMover.OuterSingleton)
		{
			UECodeGen_Private::ConstructUClass(Z_Registration_Info_UClass_ARobotMover.OuterSingleton, Z_Construct_UClass_ARobotMover_Statics::ClassParams);
		}
		return Z_Registration_Info_UClass_ARobotMover.OuterSingleton;
	}
	template<> ROBOTPROJ_API UClass* StaticClass<ARobotMover>()
	{
		return ARobotMover::StaticClass();
	}
	DEFINE_VTABLE_PTR_HELPER_CTOR(ARobotMover);
	ARobotMover::~ARobotMover() {}
	struct Z_CompiledInDeferFile_FID_Capstone_Digital_Twin_CS_Capstone_Unreal_CPP_Files_RobotProj_Source_RobotProj_RobotMover_h_Statics
	{
		static const FClassRegisterCompiledInInfo ClassInfo[];
	};
	const FClassRegisterCompiledInInfo Z_CompiledInDeferFile_FID_Capstone_Digital_Twin_CS_Capstone_Unreal_CPP_Files_RobotProj_Source_RobotProj_RobotMover_h_Statics::ClassInfo[] = {
		{ Z_Construct_UClass_ARobotMover, ARobotMover::StaticClass, TEXT("ARobotMover"), &Z_Registration_Info_UClass_ARobotMover, CONSTRUCT_RELOAD_VERSION_INFO(FClassReloadVersionInfo, sizeof(ARobotMover), 2264097746U) },
	};
	static FRegisterCompiledInInfo Z_CompiledInDeferFile_FID_Capstone_Digital_Twin_CS_Capstone_Unreal_CPP_Files_RobotProj_Source_RobotProj_RobotMover_h_5976307(TEXT("/Script/RobotProj"),
		Z_CompiledInDeferFile_FID_Capstone_Digital_Twin_CS_Capstone_Unreal_CPP_Files_RobotProj_Source_RobotProj_RobotMover_h_Statics::ClassInfo, UE_ARRAY_COUNT(Z_CompiledInDeferFile_FID_Capstone_Digital_Twin_CS_Capstone_Unreal_CPP_Files_RobotProj_Source_RobotProj_RobotMover_h_Statics::ClassInfo),
		nullptr, 0,
		nullptr, 0);
PRAGMA_ENABLE_DEPRECATION_WARNINGS
