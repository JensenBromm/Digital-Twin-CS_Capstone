// Fill out your copyright notice in the Description page of Project Settings.


#include "RobotMover.h"

#include "AsyncTreeDifferences.h"
#include "Public/DatabaseConnection.h"
THIRD_PARTY_INCLUDES_START
#include <vector>
#include <cstdlib>
#include <memory>
#include <mongocxx/pool.hpp>
#include <mongocxx/database.hpp>
#include <bsoncxx/builder/basic/array.hpp>
#include <bsoncxx/builder/basic/document.hpp>
#include <bsoncxx/builder/basic/kvp.hpp>
#include <bsoncxx/json.hpp>
THIRD_PARTY_INCLUDES_END

using bsoncxx::builder::basic::kvp;
using bsoncxx::builder::basic::make_array;
using bsoncxx::builder::basic::make_document;
using bsoncxx::stdx::string_view;

// Sets default values
ARobotMover::ARobotMover()
{
 	// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	PrimaryActorTick.bCanEverTick = true;
}

// Called when the game starts or when spawned
void ARobotMover::BeginPlay()
{
	Super::BeginPlay();

	startLocation = GetActorLocation();
	std::string name = std::string(TCHAR_TO_UTF8(*GetActorLabel()));
	int length = name.size();
	_id = name.substr(length - 1);
	//UE_LOG(LogTemp, Log, TEXT("%hs"), _id.c_str());
	className = name.substr(0, length - 2);
	//UE_LOG(LogTemp, Log, TEXT("%hs"), className.c_str());
}

// Called every frame
void ARobotMover::Tick(float DeltaTime)
{
	Super::Tick(DeltaTime);

	MoveRobot(DeltaTime);
	if (DatabaseClass)
	{
		//TODO Pass in collection instead of cursor
		getRobotInfo(DatabaseClass->GetDefaultObject<ADatabaseConnection>()->getRobotDocument(_id));
	}
	
}

void ARobotMover::MoveRobot(float DeltaTime)
{
	FVector currentLocat = GetActorLocation();
	SetActorLocation(currentLocat);

	startLocation.X = x;
	startLocation.Y = z;
	SetActorLocation(startLocation);
}

void ARobotMover::getRobotInfo(std::optional<bsoncxx::document::value> cursor)
{
	auto xCoord = cursor.value().view()["x"];
	auto zCoord = cursor.value().view()["z"];
	auto name = cursor.value().view()["class"];
	tempClassName = bsoncxx::types::b_string(name.get_string().value);
	x = bsoncxx::types::b_double(xCoord.get_double().value);
	z = bsoncxx::types::b_double(zCoord.get_double().value);
	dbClassName = UTF8_TO_TCHAR(tempClassName.c_str());
	//UE_LOG(LogTemp, Log, TEXT("%hs"), dbClassName.c_str());
}