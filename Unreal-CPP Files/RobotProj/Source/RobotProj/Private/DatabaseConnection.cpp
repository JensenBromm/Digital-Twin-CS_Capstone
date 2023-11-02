// Fill out your copyright notice in the Description page of Project Settings.


#include "RobotProj/Public/DatabaseConnection.h"
#include "MongoInstance.h"
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
ADatabaseConnection::ADatabaseConnection()
{
 	// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	PrimaryActorTick.bCanEverTick = true;
	MongoInstance::GetInstance()->createPool(getenv("URI"));
	auto dbClient = MongoInstance::GetInstance()->getClientFromPool();
	robotDocument = dbClient->database("Capstone").collection("robots");
}

// Called when the game starts or when spawned
void ADatabaseConnection::BeginPlay()
{
	Super::BeginPlay();
	SetActorTickInterval(0.2f);
}

// Called every frame
void ADatabaseConnection::Tick(float DeltaTime)
{
	Super::Tick(DeltaTime);
	
	createdDocument = true;
}

std::optional<bsoncxx::document::value> ADatabaseConnection::getRobotDocument(std::string robotClass)
{
	return robotDocument.find_one(make_document(kvp("_id", std::stoi(robotClass))));
}

bool ADatabaseConnection::getDocumentStatus()
{
	return createdDocument;
}


